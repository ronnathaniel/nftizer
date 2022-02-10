
import nftizer
from nftizer.const import SMCOLON, TAB, ENDL, IS_OWNER_ADDED


def section_license_identifer():
    section = '// SPDX-License-Identifier: MIT' + ENDL

    return section


def section_pramga(_version=None):
    version = '0.8.0'
    if isinstance(_version, str) and _version.count('.') == 2:
        version = _version
    section = 'pragma solidity >=' + version + SMCOLON + ENDL + ENDL

    return section


def section_import_ownable():
    # section = """import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v2.5.0/contracts/ownership/Ownable.sol";""" + ENDL
    section = """import "openzeppelin/contracts/access/Ownable.sol";""" + ENDL

    # with open("../node_modules/@openzeppelin/contracts/access/Ownable.sol", 'r') as fh:
    #     print(fh.read())
    return section


def section_import_token_meta():
    # section = """import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v2.5.0/contracts/token/ERC721/ERC721MetadataMintable.sol";""" + ENDL
    section = """import "nibbstack/erc721/src/contracts/tokens/nf-token-metadata.sol";""" + ENDL

    return section


def section_contract_open(_contract_name: str):
    section = ENDL + 'contract {_contract_name} is NFTokenMetadata, Ownable {{'.format(
        _contract_name=_contract_name) + ENDL

    return section


def section_contract_close():
    section = '}' + ENDL

    return section

def section_state_vars():
    section = TAB + (('address private samoOwner' + SMCOLON + ENDL) if IS_OWNER_ADDED else '') + \
        ENDL

    return section


def section_constructor_open():
    section = TAB + 'constructor() {' + ENDL

    return section


def section_constructor_body(_nft_name: str, _nft_symbol: str):
    section = TAB + TAB + 'nftName = "{_nft_name}"'.format(_nft_name=_nft_name) + SMCOLON + ENDL + \
              TAB + TAB + 'nftSymbol = "{_nft_symbol}"'.format(_nft_symbol=_nft_symbol) + SMCOLON + ENDL + \
              ((TAB + TAB + 'samoOwner = msg.sender' + SMCOLON + ENDL) if IS_OWNER_ADDED else '')

    return section


def section_constructor_close():
    section = TAB + '}' + ENDL + ENDL

    return section


def section_function_mint():
    section = TAB + 'function mint(' + ENDL + \
              TAB + TAB + 'address _to,' + ENDL + \
              TAB + TAB + 'uint256 _tokenID,' + ENDL + \
              TAB + TAB + 'string calldata _uri' + ENDL + \
              TAB + ') external onlyOwner {' + ENDL + \
              TAB + TAB + 'super._mint(_to, _tokenID);' + ENDL + \
              TAB + TAB + 'super._setTokenUri(_tokenID, _uri);' + ENDL + \
              TAB + '}' + ENDL + ENDL

    return section
