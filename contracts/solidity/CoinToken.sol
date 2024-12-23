// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract CoinToken is ERC20 {
    address public governance;

    constructor(uint256 initialSupply, address _governance) ERC20("Coin AI Token", "COIN") {
        _mint(msg.sender, initialSupply);
        governance = _governance;
    }

    function setGovernance(address _newGov) external {
        require(msg.sender == governance, "Not authorized");
        governance = _newGov;
    }
}
