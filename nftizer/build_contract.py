
import time
from typing import Union

from nftizer import sections_contract as sections


def options_default() -> Union[dict]:
    unixtime = str(int(time.time()))
    return {
        'f_path': 'SAMOContract.sol',
        'contract_name': 'SAMOContract',
        'nft_name': 'SAMONFT',
        'nft_symbol': 'SAMOSYMB',
    }


def build(options):
    f_path = options.get('f_path')
    contract_name = options.get('contract_name')
    nft_name = options.get('nft_name')
    nft_symbol = options.get('nft_symbol')

    with open(f_path, 'w+') as fh:
        fh.write(sections.section_license_identifer())
        fh.write(sections.section_pramga())
        fh.write(sections.section_import_token_meta())
        fh.write(sections.section_import_ownable())
        fh.write(sections.section_contract_open(contract_name))
        fh.write(sections.section_state_vars())
        fh.write(sections.section_constructor_open())
        fh.write(sections.section_constructor_body(nft_name, nft_symbol))
        fh.write(sections.section_constructor_close())
        fh.write(sections.section_function_mint())
        fh.write(sections.section_contract_close())


if __name__ == '__main__':
    build(options_default())