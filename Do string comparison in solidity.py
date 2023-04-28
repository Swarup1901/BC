pragma solidity ^0.8.0;
contract Demo{
    string str1="rifath";
    string str2='rifath”';
    bool public isEqual;
    function cmp() public
    {
        isEqual=keccak256(abi.encodePacked(str1))==keccak256(abi.encodePacked(str2));
    }
}
