import io
from unittest import TestCase
from unittest.mock import patch
from game import combat_round


class TestCombatRound(TestCase):

    @patch('random.randint', side_effect=[30, 15, 3, 10, 15, 30, 15, 1])
    @patch('builtins.input', side_effect=["k"])
    def test_foe_hp_updated_after_round(self, mock_input, mock_randint):
        character = {"hp": 30, 'level': 1, 'exp': 250, 'location': [3, 1], "min_damage": 15, "max_damage": 20}
        foe = {"name": 'walder', "hp": 30, "min_damage": 5, "max_damage": 15}
        action = "k"
        combat_round(character, foe, action)
        expected = 15
        self.assertEqual(expected, foe['hp'])

    @patch('random.randint', side_effect=[30, 40, 3, 10, 10])
    def test_user_hp_less_equal_than_zero_when_dead(self, mock_randint):
        character = {"hp": 10, 'level': 1, 'exp': 250, 'location': [3, 2], "min_damage": 14, "max_damage": 20}
        foe = {"name": 'walder', "hp": 30, "min_damage": 5, "max_damage": 15}
        action = "k"
        combat_round(character, foe, action)
        self.assertLessEqual(character['hp'], 0)

    @patch('random.randint', side_effect=[30, 15, 3, 10, 10])
    def test_foe_hp_less_equal_than_zero_when_dead(self, mock_randint):
        character = {"hp": 10, 'level': 1, 'exp': 250, 'location': [3, 3], "min_damage": 15, "max_damage": 21,
                     'exp_required_to_level': 500}
        foe = {"name": 'walder', "hp": 10, "min_damage": 5, "max_damage": 15}
        action = "k"
        combat_round(character, foe, action)
        self.assertLessEqual(foe['hp'], 0)

    @patch('random.randint', side_effect=[30, 15, 1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_foe_runway(self, mock_stdout, mock_randint):
        character = {"hp": 30, 'level': 1, 'exp': 250, 'location': [3, 3], "min_damage": 15, "max_damage": 20}
        foe = {"name": 'walder', "hp": 30, "min_damage": 5, "max_damage": 15}
        action = "k"
        combat_round(character, foe, action)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = "walder ran away!!!\n" \
                          "[Current Status: LEVEL [92m1[00m, [92m250[00m EXP[92m30[00m HP ]\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', side_effect=[30, 15, 3, 40])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_try_to_runway_success(self, mock_stdout, mock_randint):
        character = {"hp": 30, 'level': 1, 'exp': 250, 'location': [3, 3], "min_damage": 15, "max_damage": 21}
        foe = {"name": 'walder', "hp": 30, "min_damage": 5, "max_damage": 15}
        action = "no"
        combat_round(character, foe, action)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = "You attempt to run!\n" \
                          ".\n" \
                          ".\n" \
                          ".\n" \
                          ".\n" \
                          "You got away successfully!\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', side_effect=[30, 15, 3, 10, 8])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_try_fail_to_flee(self, mock_stdout, mock_randint):
        character = {"hp": 30, 'level': 1, 'exp': 250, 'location': [3, 4], "min_damage": 15, "max_damage": 20}
        foe = {"name": 'walder', "hp": 30, "min_damage": 5, "max_damage": 15}
        action = "no"
        combat_round(character, foe, action)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = "You attempt to run!\n" \
                          ".\n" \
                          ".\n" \
                          ".\n" \
                          ".\n" \
                          "You got away successfully!\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', side_effect=[30, 15, 3, 10, 15, 30, 15, 1])
    @patch('builtins.input', side_effect=["k"])
    def test_character_hp_not_change_if_foe_feeling(self, mock_input, mock_randint):
        character = {"hp": 30, 'level': 1, 'exp': 250, 'location': [4, 5], "min_damage": 15, "max_damage": 20}
        foe = {"name": 'walder', "hp": 30, "min_damage": 5, "max_damage": 15}
        action = "k"
        combat_round(character, foe, action)
        expected = 30
        self.assertEqual(expected, character['hp'])

    @patch('random.randint', side_effect=[30, 15, 3, 10, 15, 30, 15, 1])
    @patch('builtins.input', side_effect=["k"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_info_correct_when_foe_flee_after_one_round(self, mock_stdout, mock_input, mock_randint):
        character = {"hp": 30, 'level': 1, 'exp': 250, 'location': [3, 5], "min_damage": 15, "max_damage": 20}
        foe = {"name": 'walder', "hp": 30, "min_damage": 5, "max_damage": 15}
        action = "k"
        combat_round(character, foe, action)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = "You attacked walder. The demon lost 15 HP\n" \
                          "[Current Status: LEVEL [92m1[00m, [92m250[00m EXP, [92m30[00m HP ]\n" \
                          "walder ran away!!!\n" \
                          "[Current Status: LEVEL [92m1[00m, [92m250[00m EXP[92m30[00m HP ]\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', side_effect=[30, 40, 3, 10, 10])
    def test_hp_updated_correct_user_dead_after_round(self, mock_randint):
        character = {"hp": 10, 'level': 1, 'exp': 250, 'location': [3, 7], "min_damage": 15, "max_damage": 20}
        foe = {"name": 'walder', "hp": 30, "min_damage": 5, "max_damage": 15}
        action = "k"
        combat_round(character, foe, action)
        self.assertLessEqual(character['hp'], 0)

    @patch('random.randint', side_effect=[30, 40, 3, 10, 10])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_correct_when_user_dead(self, mock_stdout, mock_randint):
        character = {"hp": 10, 'level': 1, 'exp': 250, 'location': [3, 6], "min_damage": 15, "max_damage": 20}
        foe = {"name": 'walder', "hp": 30, "min_damage": 5, "max_damage": 15}
        action = "k"
        combat_round(character, foe, action)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = "The walder attacked you. You lost 10 HP\n" \
                          "[1;31mYou were defeated by walder [0m\n\n" \
                          """[1;31m
    #     #                  ######                  
     #   #   ####  #    #    #     # # ###### #####  
      # #   #    # #    #    #     # # #      #    # 
       #    #    # #    #    #     # # #####  #    # 
       #    #    # #    #    #     # # #      #    # 
       #    #    # #    #    #     # # #      #    # 
       #     ####   ####     ######  # ###### #####  
                                                  
                                                    
    [0m\n""" \
                          "** You failed to save the Pokemon. They continue to be experimented on. **\n"

        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', side_effect=[30, 15, 3, 10, 10])
    def test_foe_hp_equal_less_than_zero_when_dead_after_one_round(self, mock_randint):
        character = {"hp": 10, 'level': 1, 'exp': 250, 'location': [4, 7], "min_damage": 15, "max_damage": 20,
                     'exp_required_to_level': 500}
        foe = {"name": 'walder', "hp": 10, "min_damage": 5, "max_damage": 15}
        action = "k"
        combat_round(character, foe, action)
        self.assertLessEqual(foe['hp'], 0)

    @patch('random.randint', side_effect=[30, 15, 3, 10, 10])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_correct_message_when_foe_dead_after_round(self, mock_stdout, mock_randint):
        character = {"hp": 10, 'level': 1, 'exp': 250, 'location': [3, 7], "min_damage": 15, "max_damage": 20,
                     'exp_required_to_level': 500}
        foe = {"name": 'walder', "hp": 10, "min_damage": 5, "max_damage": 15}
        action = "k"
        combat_round(character, foe, action)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = "You attacked walder. The demon lost 10 HP\n" \
                          "[1;35mThe walder has been defeated[0m\n" \
                          "You gained [92m150[00m exp from this battle!\n" \
                          "[Current Status: LEVEL [92m1[00m, [92m400[00m EXP, [92m10[00m HP ]\n"
        self.assertEqual(expected_output, the_game_printed_this)
