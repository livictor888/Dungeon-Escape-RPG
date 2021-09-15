import io
from unittest import TestCase
from unittest.mock import patch

from game import display_character_health


@patch('sys.stdout', new_callable=io.StringIO)
class TestDisplayCharacterHealth(TestCase):
    def test_display_level_one_information(self, mock_stdout):
        character = {'level_one_name': "Squirtle", 'class_name': 'Water', "hp": 20, 'level': 1, 'exp': 250,
                     'location': [3, 3], "min_damage": 15, "max_damage": 20}
        display_character_health(character)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = "[Current HP: 20, your Pokemon: Squirtle]\n"
        self.assertEqual(expected_output, the_game_printed_this)

    def test_display_level_two_information(self, mock_stdout):
        character = {'level_two_name': "Warturtle", 'class_name': 'Water', "hp": 20, 'level': 2, 'exp': 250,
                     'location': [3, 3], "min_damage": 15, "max_damage": 20}
        display_character_health(character)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = "[Current HP: 20, your Pokemon: Warturtle]\n"
        self.assertEqual(expected_output, the_game_printed_this)

    def test_display_level_three_information(self, mock_stdout):
        character = {'level_three_name': "Blastoise", 'class_name': 'Water', "hp": 20, 'level': 3, 'exp': 250,
                     'location': [3, 3], "min_damage": 15, "max_damage": 20}
        display_character_health(character)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = "[Current HP: 20, your Pokemon: Blastoise]\n"
        self.assertEqual(expected_output, the_game_printed_this)
