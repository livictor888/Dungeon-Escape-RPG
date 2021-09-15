import io
from unittest import TestCase
from unittest.mock import patch
from game import combat_round_with_boss


class TestCombatRoundWithBoss(TestCase):

    @patch('random.randint', side_effect=[30, 15, 30, 30])
    def test_is_character_hp_great_than_zero_when_defeat_boss(self, mock_randint):
        boss = {'hp': 30, 'location': [5, 5], "min_damage": 20, "max_damage": 30}
        character = {"hp": 30, 'level': 3, 'exp': 650, 'location': [3, 3], "min_damage": 20, "max_damage": 30}
        combat_round_with_boss(character, boss)
        self.assertGreater(character['hp'], 0)

    @patch('random.randint', side_effect=[15, 30, 30, 30])
    def test_is_boss_hp_great_than_zero_when_character_dead(self, mock_randint):
        boss = {'hp': 30, 'location': [5, 5], "min_damage": 20, "max_damage": 30}
        character = {"hp": 30, 'level': 3, 'exp': 650, 'location': [3, 3], "min_damage": 20, "max_damage": 30}
        combat_round_with_boss(character, boss)
        self.assertGreater(boss['hp'], 0)

    @patch('random.randint', side_effect=[30, 15, 30, 30])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_if_character_defeats_boss(self, mock_stdout, mock_randint):
        boss = {'hp': 30, 'location': [5, 5], "min_damage": 20, "max_damage": 30}
        character = {"hp": 30, 'level': 3, 'exp': 650, 'location': [3, 3], "min_damage": 20, "max_damage": 30}
        combat_round_with_boss(character, boss)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = "You attacked the Boss. The boss lost 30 HP.\n" \
                          "[1;35mThe Boss has been defeated![0m. \n" \
                          " You have saved all the Pokemon!\n\n" \
                          """[1;33m
    #     #                               #######                               
    #     #   ##   #####  #####  #   #    #       #    # #####  # #    #  ####  
    #     #  #  #  #    # #    #  # #     #       ##   # #    # # ##   # #    # 
    ####### #    # #    # #    #   #      #####   # #  # #    # # # #  # #      
    #     # ###### #####  #####    #      #       #  # # #    # # #  # # #  ### 
    #     # #    # #      #        #      #       #   ## #    # # #   ## #    # 
    #     # #    # #      #        #      ####### #    # #####  # #    #  ####  
                                                                             
    [0m\n"""

        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', side_effect=[15, 30, 30, 30])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_if_character_dead(self, mock_stdout, mock_randint):
        boss = {'hp': 30, 'location': [5, 5], "min_damage": 20, "max_damage": 30}
        character = {"hp": 30, 'level': 3, 'exp': 650, 'location': [3, 3], "min_damage": 20, "max_damage": 30}
        combat_round_with_boss(character, boss)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = "The Boss attacked you. You lost 30 HP\n\n" \
                          """[1;31m
    #     #                  ######                  
     #   #   ####  #    #    #     # # ###### #####  
      # #   #    # #    #    #     # # #      #    # 
       #    #    # #    #    #     # # #####  #    # 
       #    #    # #    #    #     # # #      #    # 
       #    #    # #    #    #     # # #      #    # 
       #     ####   ####     ######  # ###### #####  
                                                  
                                                    
    [0m
** You failed to save the Pokemon. They continue to be experimented on. **\n"""

        self.assertEqual(expected_output, the_game_printed_this)
