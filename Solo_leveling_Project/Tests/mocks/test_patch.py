from fights import fights_
from Classes import *
from unittest.mock import patch

def test_patch_fights():
    player = Mock()
    sleh = Mock()
    deraa = Mock()
    nunu = Mock()
    nunu.health = 100  
    with patch('__main__.time.sleep'):
        with patch('__main__.open'), patch('builtins.input', side_effect=['a']):
            result = fights_(player, sleh, deraa)
    assert result == "finished"  
