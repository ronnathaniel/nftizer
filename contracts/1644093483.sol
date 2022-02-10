// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

import "https://github.com/nibbstack/erc721/src/contracts/tokens/nf-token-metadata.sol";
import "https://github.com/nibbstack/erc721/src/contracts/ownership/ownable.sol";

contract Cont1644093483 is NFTokenMetadata, Ownable {
	constructor() {
		nftName = "NFT1644093483";
		nftSymbol = "Symbol1644093483";
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
