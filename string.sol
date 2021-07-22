pragma solidity >0.5.0;

contract Learning {
    string public name = "string"; 

    function set(string memory _value) public {
        name = _value;
    }

}