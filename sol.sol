pragma solidity >0.5.0;

contract learning {
   

    function hello() public returns (string memory){
        return "Hello World";
    }

    function multiplication(uint _var) public returns (uint){
     uint varl = _var * 10;

     return varl;
    
    }
}