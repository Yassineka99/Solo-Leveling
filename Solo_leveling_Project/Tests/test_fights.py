from fights import fights_
from Classes import *

def test_fights_():#    INPUTS REQUIRED INSIDE THE FUNCTIONS IN FIGHTS_ 
    player=Ninja()
    sleh=Katana()
    deraa=waterarmor()
    result=fights_(player,sleh,deraa)
    assert result == 'not finished' 
    player=Paladin()
    sleh=Axe()
    deraa=firearmor()
    result=fights_(player,sleh,deraa)
    assert result == 'not finished' 
    player=Viking()
    sleh=Machete()
    deraa=eartharmor()
    result=fights_(player,sleh,deraa)
    assert result == 'not finished' 
    player=Barbarian()
    sleh=Sword()
    deraa=airarmor()
    result=fights_(player,sleh,deraa)
    assert result == 'not finished' 
