pragma solidity >=0.5.0 <0.9.0;
//rifath 3
   contract Demo{
      string public s1 = "RIFATH ";
      string public s2 = "ZAHRAA";
      string public new_str;

      function concatenate() public {
         new_str = string(abi.encodePacked(s1, s2));
       }
}
