from fights import fights_
from Classes import *
from unittest.mock import Mock
def test_mock_return_value_fights():
    player = Mock()
    sleh = Mock()
    deraa = Mock()
    nunu = Mock()
    nunu.health = 100  
    player.health = 100  
    player.dammage = 10  
    nunu.rewards = 50  
    nunu.dammage = 20  
    with patch('__main__.time.sleep'):
        with patch('__main__.open'), patch('builtins.input', side_effect=['a']):
            result = fights_1(player, sleh, deraa, nunu)
    assert result == True  