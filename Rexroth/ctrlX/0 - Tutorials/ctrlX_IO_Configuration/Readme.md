# Quick Example on how to setups IOs


### PLC variables:

    IN0:BOOL:=True;
        
    IN2:BOOL;
        
    OUT2:BOOL;
        
    timerToOn: TON;
    timerToOff: TON;
    timeOn:BOOL;
    timeOff:BOOL;
        
    timer:TIME:=T#1S;

### PLC Program

    //changing the timer with input #0
    IF IN0 THEN
        timer:=T#1S;
    ELSE
        timer:=T#5S;	
    END_IF

    //setting Up output #2 ON timer
    timerToOn(IN:= NOT IN2, PT:= timer, Q=> timeOn, ET=> );

    //setting Up output #2 IFF timer
    timerToOff(IN:= IN2, PT:= timer, Q=> timeOff, ET=> );

    // Setup output 2 to true if timeON variable is true
    IF timeOn THEN
        OUT2:=TRUE;
    END_IF

    // Setup output 2 to true if timeOff variable is true
    IF timeOff THEN
        OUT2:=FALSE;
    END_IF