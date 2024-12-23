// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract Marketplace {
    IERC20 public token;
    address public owner;

    struct Item {
        uint256 id;
        address seller;
        string name;
        uint256 price;
        bool sold;
    }

    uint256 public itemCount;
    mapping(uint256 => Item) public items;

    event ItemListed(uint256 id, address seller, string name, uint256 price);
    event ItemPurchased(uint256 id, address buyer, address seller, uint256 price);
    event ItemRemoved(uint256 id, address seller);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    modifier onlySeller(uint256 _itemId) {
        require(items[_itemId].seller == msg.sender, "Not the seller");
        _;
    }

    constructor(IERC20 _token) {
        token = _token;
        owner = msg.sender;
    }

    function listItem(string memory _name, uint256 _price) external {
        require(_price > 0, "Price must be greater than zero");

        itemCount++;
        items[itemCount] = Item({
            id: itemCount,
            seller: msg.sender,
            name: _name,
            price: _price,
            sold: false
        });

        emit ItemListed(itemCount, msg.sender, _name, _price);
    }

    function buyItem(uint256 _itemId) external {
        Item storage item = items[_itemId];
        require(item.id > 0, "Item does not exist");
        require(!item.sold, "Item already sold");
        require(token.balanceOf(msg.sender) >= item.price, "Insufficient funds");

        // Transfer tokens from buyer to seller
        token.transferFrom(msg.sender, item.seller, item.price);

        // Mark item as sold
        item.sold = true;

        emit ItemPurchased(_itemId, msg.sender, item.seller, item.price);
    }

    function removeItem(uint256 _itemId) external onlySeller(_itemId) {
        Item storage item = items[_itemId];
        require(!item.sold, "Sold items cannot be removed");

        delete items[_itemId];

        emit ItemRemoved(_itemId, msg.sender);
    }

    function setToken(IERC20 _token) external onlyOwner {
        token = _token;
    }
}
