import io
import random
from unittest import TestCase
from unittest.mock import patch

from game import attack


class TestAttack(TestCase):
    def test_foe_strike_power_range_correct(self):
        character_speed = 10
        foe_speed = 30
        character = {"hp": 30, 'level': 1, 'exp': 250, 'location': [3, 3], "min_damage": 15, "max_damage": 20}
        foe = {"name": 'walder', "hp": 30, "min_damage": 5, "max_damage": 15}
        attack(character_speed, foe_speed, character, foe)
        foe_damage = random.randint(foe["min_damage"], foe["max_damage"])
        self.assertGreaterEqual(foe_damage, foe['min_damage'])
        self.assertLessEqual(foe_damage, foe['max_damage'])

    def test_character_strike_power_range_correct(self):
        character_speed = 10
        foe_speed = 30
        character = {"hp": 30, 'level': 1, 'exp': 250, 'location': [3, 3], "min_damage": 15, "max_damage": 20}
        foe = {"name": 'walder', "hp": 30, "min_damage": 5, "max_damage": 15}
        attack(character_speed, foe_speed, character, foe)
        character_damage = random.randint(character["min_damage"], character["max_damage"])
        self.assertGreaterEqual(character_damage, character['min_damage'])
        self.assertLessEqual(character_damage, character['max_damage'])

    @patch('random.randint', side_effect=[5, 15])
    def test_foe_strike_first_but_character_alive_after_being_attacked(self, mocked_damage):
        character_speed = 10
        foe_speed = 30
        character = {"hp": 30, 'level': 1, 'exp': 250, 'location': [3, 3], "min_damage": 15, "max_damage": 20}
        foe = {"name": 'walder', "hp": 30, "min_damage": 5, "max_damage": 15}
        attack(character_speed, foe_speed, character, foe)
        self.assertGreater(character['hp'], 0)

    @patch('random.randint', side_effect=[5, 15])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_combat_result_correct_after_character_being_attacked(self, mock_stdout, mocked_damage):
        character_speed = 10
        foe_speed = 30
        character = {"hp": 30, 'level': 1, 'exp': 250, 'location': [3, 3], "min_damage": 15, "max_damage": 20}
        foe = {"name": 'walder', "hp": 30, "min_damage": 5, "max_damage": 15}
        attack(character_speed, foe_speed, character, foe)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = 'The walder attacked you. You lost 5 HP\n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', side_effect=[5, 15])
    def test_character_attack_first_but_foe_alive_after_being_attacked(self, mocked_damage):
        character_speed = 30
        foe_speed = 10
        character = {"hp": 30, 'level': 1, 'exp': 250, 'location': [3, 3], "min_damage": 15, "max_damage": 20}
        foe = {"name": 'walder', "hp": 30, "min_damage": 5, "max_damage": 15}
        attack(character_speed, foe_speed, character, foe)
        self.assertGreater(foe['hp'], 0)

    @patch('random.randint', side_effect=[5, 15])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_combat_result_correct_after_foe_being_attacked(self, mock_stdout, mocked_damage):
        character_speed = 30
        foe_speed = 10
        character = {"hp": 30, 'level': 1, 'exp': 250, 'location': [3, 3], "min_damage": 15, "max_damage": 20}
        foe = {"name": 'walder', "hp": 30, "min_damage": 5, "max_damage": 15}
        attack(character_speed, foe_speed, character, foe)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = 'You attacked walder. The demon lost 15 HP\n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', side_effect=[5, 15])
    def test_character_attack_and_foe_dead(self, mocked_damage):
        character_speed = 30
        foe_speed = 10
        character = {"hp": 30, 'level': 1, 'exp': 250, 'location': [3, 3], "min_damage": 15, "max_damage": 20}
        foe = {"name": 'walder', "hp": 15, "min_damage": 5, "max_damage": 15}
        attack(character_speed, foe_speed, character, foe)
        self.assertLessEqual(foe['hp'], 0)

    @patch('random.randint', side_effect=[5, 15])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_foe_dead_message_correct(self, mock_stdout, mocked_damage):
        character_speed = 30
        foe_speed = 10
        character = {"hp": 30, 'level': 1, 'exp': 250, 'location': [3, 3], "min_damage": 15, "max_damage": 20}
        foe = {"name": 'walder', "hp": 15, "min_damage": 5, "max_damage": 15}
        attack(character_speed, foe_speed, character, foe)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = 'You attacked walder. The demon lost 15 HP\n'\
            '[1;35mThe walder has been defeated[0m\n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', side_effect=[30, 5])
    def test_foe_attack_and_character_dead(self, mocked_damage):
        character_speed = 10
        foe_speed = 30
        character = {"hp": 30, 'level': 1, 'exp': 250, 'location': [3, 3], "min_damage": 15, "max_damage": 20}
        foe = {"name": 'walder', "hp": 15, "min_damage": 5, "max_damage": 15}
        attack(character_speed, foe_speed, character, foe)
        self.assertLessEqual(character['hp'], 0)

    @patch('random.randint', side_effect=[15, 15])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_dead_message_correct(self, mock_stdout, mocked_damage):
        character_speed = 10
        foe_speed = 30
        character = {"hp": 15, 'level': 1, 'exp': 250, 'location': [3, 3], "min_damage": 15, "max_damage": 20}
        foe = {"name": 'walder', "hp": 30, "min_damage": 5, "max_damage": 15}
        attack(character_speed, foe_speed, character, foe)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = """The walder attacked you. You lost 15 HP
[1;31mYou were defeated by walder [0m

[1;31m
    #     #                  ######                  
     #   #   ####  #    #    #     # # ###### #####  
      # #   #    # #    #    #     # # #      #    # 
       #    #    # #    #    #     # # #####  #    # 
       #    #    # #    #    #     # # #      #    # 
       #    #    # #    #    #     # # #      #    # 
       #     ####   ####     ######  # ###### #####  
                                                  
                                                    
    [0m
** You failed to save the Pokemon. They continue to be experimented on. **
"""
        self.assertEqual(expected_output, the_game_printed_this)
