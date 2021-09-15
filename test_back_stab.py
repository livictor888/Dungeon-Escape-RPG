from unittest import TestCase
from unittest.mock import patch
from game import back_stab
import random


class TestBackStab(TestCase):
    # checking the number of chance is in correct range by roll dies million times
    def test_chance_of_back_stabbed_correct(self):
        number_of_roll = 10000000
        percentage_of_back_stab = 20
        result = [random.randint(1, 100) for _ in range(number_of_roll)]
        number_for_stabbed = []
        for i in result:
            if i <= 20:
                number_for_stabbed.append(i)
        expected_chance = percentage_of_back_stab
        actual_chance = len(number_for_stabbed) * 100 / number_of_roll
        self.assertAlmostEqual(expected_chance, actual_chance, 1)

    @patch("random.randint", return_value=30)
    def test_no_back_stab(self, mock_randint):
        character = dict(hp=20, level=1, exp=250)
        foe = dict(name="Walder", min_damage=10, max_damage=15)
        actual = back_stab(character, foe)
        expected_return = False
        self.assertEqual(expected_return, actual)
        self.assertEqual(character["hp"], 20)

    @patch('random.randint', side_effect=[5, 5])  # get back stabbed, foe does 5 damage
    def test_character_takes_back_stab_damage(self, mock_randint):
        foe = dict(name="Walder",
                   hp=10,
                   min_damage=5,
                   max_damage=15)
        character = dict(hp=20, level=1, exp=250)
        actual = back_stab(character, foe)
        expected_return = True
        self.assertEqual(actual, expected_return)  # got back stabbed
        self.assertEqual(character["hp"], 15)  # character takes 5 damage

    @patch('random.randint', side_effect=[5, 5])  # get back stabbed, foe does 5 damage
    def test_back_stab_attack_power_correct(self, mock_randint):
        foe = dict(name="Walder",
                   hp=10,
                   min_damage=5,
                   max_damage=15)
        character = dict(hp=20, level=1, exp=250)
        back_stab(character, foe)
        actual_power = 5
        self.assertGreaterEqual(actual_power, foe['min_damage'])
        self.assertLessEqual(actual_power, foe['max_damage'])

    @patch('random.randint', side_effect=[5, random.randint(5, 15)])  # get back stabbed, foe does 5-15 damage
    def test_get_back_stabbed_in_correct_damage_range(self, mock_back_stab_chance):
        foe = dict(name="Walder",
                   hp=10,
                   min_damage=5,
                   max_damage=15)
        character = dict(hp=20, level=1, exp=250)
        actual = back_stab(character, foe)
        expected_return = True
        expected_damage_range = range(5, 15+1)
        self.assertEqual(actual, expected_return)  # got back stabbed
        self.assertIn(character["hp"], expected_damage_range)


