pragma solidity ^0.5.12;
contract Test{
    function callsha256() public pure returns(bytes32 result){
        return sha256("rifath");
    }
    function callkeccak256() public pure returns(bytes32 result){
        return keccak256("rifath");
    }
}
