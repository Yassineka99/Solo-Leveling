from fights import fights_
from Classes import *
from unittest.mock import Mock
def test_mock_side_effect_fights():
    player = Mock()
    sleh = Mock()
    deraa = Mock()
    nunu = Mock()
    nunu.health = 100  # Set initial health
    player.health = 100  # Set player's initial health
    player.dammage = 10  # Set player's initial damage
    nunu.rewards = 50  # Set rewards for Nunu
    nunu.dammage = 20  # Set Nunu's damage
    def mock_input(prompt):
        if prompt == "Do you want to add them to Hp or attack ?":
            return 'hp'
        elif prompt == "click any key to hit the monster":
            return 'a'
        else:
            return 'a'
    with patch('__main__.time.sleep'):
        with patch('__main__.open'), patch('builtins.input', side_effect=mock_input):
            result = fights_1(player, sleh, deraa, nunu)
    assert result == True  # Assuming the player wins the fight