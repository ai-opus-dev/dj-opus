// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract Migration {
    IERC20 public oldToken;
    IERC20 public newToken;
    address public owner;

    mapping(address => bool) public migrated;

    event TokensMigrated(address indexed user, uint256 amount);
    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);
    event MigrationStopped();

    bool public migrationActive;

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    modifier whenActive() {
        require(migrationActive, "Migration is stopped");
        _;
    }

    constructor(IERC20 _oldToken, IERC20 _newToken) {
        oldToken = _oldToken;
        newToken = _newToken;
        owner = msg.sender;
        migrationActive = true;
    }

    function migrate() external whenActive {
        require(!migrated[msg.sender], "Already migrated");
        
        uint256 balance = oldToken.balanceOf(msg.sender);
        require(balance > 0, "No tokens to migrate");

        // Ensure old tokens are approved for transfer
        require(oldToken.transferFrom(msg.sender, address(this), balance), "Old token transfer failed");

        // Mint or transfer new tokens to the user
        require(newToken.transfer(msg.sender, balance), "New token transfer failed");

        migrated[msg.sender] = true;

        emit TokensMigrated(msg.sender, balance);
    }

    function stopMigration() external onlyOwner {
        migrationActive = false;
        emit MigrationStopped();
    }

    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    function recoverTokens(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).transfer(owner, _amount);
    }
}
