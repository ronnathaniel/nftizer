// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0;

import "nibbstack/erc721/src/contracts/tokens/nf-token-metadata.sol";
import "openzeppelin/contracts/access/Ownable.sol";

contract SAMOContract is NFTokenMetadata, Ownable {
	address private samoOwner;

	constructor() {
		nftName = "SAMONFT";
		nftSymbol = "SAMOSYMB";
		samoOwner = msg.sender;
	}

	function mint(
		address _to,
		uint256 _tokenID,
		string calldata _uri
	) external onlyOwner {
		super._mint(_to, _tokenID);
		super._setTokenUri(_tokenID, _uri);
	}

}
