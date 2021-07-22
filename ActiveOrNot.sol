pragma solidity >0.5.0;

contract ActiveCon {
    enum State { Waiting, Ready, Active}
    State public state; 

    constructor() public {
        state = State.Waiting;
    }
    function active() public {
        state = State.Active;
    }
    function isActive() public returns (bool){
        return state == State.Active;
    }
        
}