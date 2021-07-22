pragma solidity >0.5.0;

contract Strucks {
    uint256 public peopleCount = 0; 
    mapping(uint => Person) public people; 
    address owner; 
    uint256 public timeNow = 1626884480 ;
    //if time is inferior as the timeNow then contract wont be executed and transaction will be reverted 
    modifier timePass(){
        require(block.timestamp <= timeNow);
        _;
    }
  
     
    struct Person {
        uint _id; 
        string _firstname;
        string _lastname;
    } 
    function addPerson(string memory _firstname, string memory _lastname) public timePass {
        incrementCount();
        people[peopleCount] = Person(peopleCount, _firstname, _lastname); 
    }
    function incrementCount() internal {
        peopleCount += 1;
    }
}