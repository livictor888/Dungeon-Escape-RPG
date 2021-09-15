from unittest import TestCase
from unittest.mock import patch

from game import get_character_location
from game import create_character


class Test(TestCase):
    def test_location_is_coordinate(self):
        character = dict(name='Victor', location=[1, 0], level=1, class_name='Grass', exp=0,
                         level_one_name='Bulbasaur')
        actual = get_character_location(character)
        expected = [1, 0]
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["Jess", "1"])
    def test_is_location_coordinate_list(self, mocked_user_choice):
        character = create_character()
        get_character_location(character)
        expected = list
        self.assertIs(type(character['location']), expected)

    @patch('builtins.input', side_effect=["Jess", "1"])
    def test_location_is_length_two(self, mocked_user_choice):
        character = create_character()
        actual = get_character_location(character)
        expected = 2
        self.assertEqual(len(actual), expected)

    def test_location_is_positive_int(self):
        character = dict(name='Victor', location=[1, 0], level=1)
        actual = get_character_location(character)
        expected = int
        for number in actual:
            self.assertIs(type(number), expected)

