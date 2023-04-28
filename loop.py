#while
pragma solidity ^0.8.0;
//rifath 3
contract while1{
uint[] data;
uint8 j=0;
function loop() public returns(uint[] memory)
{
    while (j<10)
    {
        j++;
        data.push(j);
    }
    return data;
}
}


#do while
pragma solidity ^0.8.0;
//rifath 3
contract doWhile1{
uint[] data;
uint8 j=0;
function loop() public returns(uint[] memory)
{
    do
    {
        j++;
        data.push(j);
    }
    while (j<10);
    return data;
}
}

#for
pragma solidity ^0.8.0;
contract ForLoop{
    function count() public pure returns(uint256){
        uint256 sum=0;
        for(uint256 i=0;i<=25;i++){
            sum+=i;
        }
        return sum;
   }}
