pragma solidity ^0.5.0;
contract LedgerBalance{
    mapping(address => uint) balance;
    mapping(address => string) name;
    function updateBalance() public returns(uint){
            balance[msg.sender]=20;
            return balance[msg.sender];
    }

    function senderInfo() public returns(string memory){
        name[msg.sender] = "rifath";
        return name[msg.sender];
    }
    function printSender() public view returns(address){
        return msg.sender;
    }
}  
