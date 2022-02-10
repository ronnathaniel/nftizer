
from solcx import compile_source, install_solc

install_solc(version='0.8.0')

class CompiledContract:
    def __init__(self, _contract_source: str, w3):
        self.source = _contract_source
        self.compiled = compile_source(
            _contract_source,
            output_values=['abi', 'bin'],
            # solc_version='0.8.0'
            import_remappings={
                'openzeppelin': '../node_modules/@openzeppelin',
                'nibbstack': '../node_modules/@nibbstack',
            }

        )
        self.id, self.interface = self.compiled.popitem()
        self.bytecode = self.interface['bin']
        self.abi = self.interface['abi']
        self.w3build = w3.eth.contract(abi=self.abi, bytecode=self.bytecode)
