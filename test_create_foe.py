from unittest import TestCase
from unittest.mock import patch

from game import create_foe
from game import FOE_NAMES
from game import create_character


class TestCreateFoe(TestCase):
    @patch('builtins.input', side_effect=["Jess", "1"])
    @patch('game.foe_appear', return_value=True)
    def test_return_is_dictionary(self, mocked_value, mocked_input):
        character = create_character()
        foe = create_foe(character)
        self.assertIs(type(foe), dict)

    @patch('builtins.input', side_effect=["Jess", "1"])
    @patch('game.foe_appear', return_value=True)
    def test_name_key_is_string(self, mocked_value, mocked_input):
        character = create_character()
        foe = create_foe(character)
        self.assertIs(type(foe["name"]), str)

    @patch('builtins.input', side_effect=["Jess", "1"])
    @patch('game.foe_appear', return_value=True)
    def test_name_key_from_FOE_NAMES(self, mocked_value, mocked_input):
        character = create_character()
        foe = create_foe(character)
        self.assertIn(foe["name"], FOE_NAMES())

    @patch('game.foe_appear', return_value=True)
    @patch('random.randint', return_value=1)
    def test_is_foe_power_correct_when_character_level_one(self, mocked_input, mocked_value):
        character = {"hp": 30, 'level': 1, 'exp': 650, 'location': [3, 3], "min_damage": 20, "max_damage": 30}
        expected = {'hp': 10, 'max_damage': 10, 'min_damage': 1, 'name': 'El Nino'}
        actual = create_foe(character)
        self.assertEqual(expected, actual)

    @patch('game.foe_appear', return_value=True)
    @patch('random.randint', return_value=1)
    def test_is_foe_power_correct_when_character_level_two(self, mocked_input, mocked_value):
        character = {"hp": 30, 'level': 2, 'exp': 650, 'location': [3, 3], "min_damage": 20, "max_damage": 30}
        expected = {'hp': 15, 'max_damage': 15, 'min_damage': 5, 'name': 'El Nino'}
        actual = create_foe(character)
        self.assertEqual(expected, actual)

    @patch('game.foe_appear', return_value=True)
    @patch('random.randint', return_value=1)
    def test_is_foe_power_correct_when_character_level_three(self, mocked_input, mocked_value):
        character = {"hp": 30, 'level': 3, 'exp': 650, 'location': [3, 3], "min_damage": 20, "max_damage": 30}
        expected = {'hp': 20, 'max_damage': 20, 'min_damage': 10, 'name': 'El Nino'}
        actual = create_foe(character)
        self.assertEqual(expected, actual)