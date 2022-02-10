// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

import "https://github.com/nibbstack/erc721/src/contracts/tokens/nf-token-metadata.sol";
import "https://github.com/nibbstack/erc721/src/contracts/ownership/ownable.sol";

contract BlissNFT is NFTokenMetadata, Ownable {

    uint32 percentToOwnerOnSell;

    constructor(
        float _percentToOwnerOnSell,
    ) {
        nftName = "BlissXP";
        nftSymbol = "BLSXP";
        percentToOwnerOnSell = _percentToOwnerOnSell
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