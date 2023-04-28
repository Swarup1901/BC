pragma solidity ^0.5.0;

contract Demo{

    string str1="College";
    string str2=" KC";

    bool public isEqual;

    function cmp() public{
        isEqual=keccak256(abi.encodePacked(str1))==keccak256(abi.encodePacked(str2));
    }
}
