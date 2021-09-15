from unittest import TestCase
from unittest.mock import patch
from game import create_character


class TestCreateCharacter(TestCase):

    @patch('builtins.input', side_effect=["Jess", "1"])
    def test_user_input_name_applied_to_dict_correct(self, mock_input):
        character = create_character()
        expect = 'Jess'
        actual = character['name']
        self.assertEqual(expect, actual)

    @patch('builtins.input', side_effect=["Jess", "1"])
    def test_default_location_correct(self, mock_input):
        character = create_character()
        expect = [0, 0]
        actual = character['location']
        self.assertEqual(expect, actual)

    @patch('builtins.input', side_effect=["Jess", "1"])
    def test_default_level_correct(self, mock_input):
        character = create_character()
        expect = 1
        actual = character['level']
        self.assertEqual(expect, actual)

    @patch('builtins.input', side_effect=["Jess", "1"])
    def test_is_returned_character_dictionary(self, mock_input):
        character = create_character()
        expect = dict
        actual = type(character)
        self.assertEqual(expect, actual)

    @patch('builtins.input', side_effect=["Jess", "1"])
    def test_if_input_value_string(self, mock_input):
        create_character()
        character_name = "Jess"
        expect = str
        actual = type(character_name)
        self.assertEqual(expect, actual)

    @patch('builtins.input', side_effect=["Jess", "1"])
    def test_update_class_to_grass_when_user_choice_one(self, mock_input):
        character = create_character()
        expected_class = "Grass"
        actual_class = character['class_name']
        self.assertEqual(expected_class, actual_class)

    @patch('builtins.input', side_effect=["Jess", "2"])
    def test_update_class_to_water_when_user_choice_two(self, mock_input):
        character = create_character()
        expected_class = "Water"
        actual_class = character['class_name']
        self.assertEqual(expected_class, actual_class)

    @patch('builtins.input', side_effect=["Jess", "3"])
    def test_update_class_to_grass_when_user_choice_three(self, mock_input):
        character = create_character()
        expected_class = "Fire"
        actual_class = character['class_name']
        self.assertEqual(expected_class, actual_class)

    @patch('builtins.input', side_effect=["Jess", "4"])
    def test_update_class_to_grass_when_user_choice_four(self, mock_input):
        character = create_character()
        expected_class = "Electric"
        actual_class = character['class_name']
        self.assertEqual(expected_class, actual_class)
