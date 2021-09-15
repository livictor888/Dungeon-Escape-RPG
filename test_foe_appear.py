from unittest import TestCase
import game
from unittest.mock import patch


class TestFoeAppear(TestCase):
    # checking the number of chance is in correct range by rolling dies ten million times
    def test_chance_of_foe_appear_correct(self):
        number_of_roll = 10000000
        percentage_of_foe_appear = 20
        result = [game.foe_appear() for _ in range(number_of_roll)]
        expected_chance = percentage_of_foe_appear
        actual_chance = result.count(True) * 100 / number_of_roll
        self.assertAlmostEqual(expected_chance, actual_chance, 1)

    @patch('random.randint', return_value=10)
    def test_foe_appear_when_roll_die_result_less_than_twenty(self, mocked_random_chance):
        expected = True
        actual = game.foe_appear()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=20)
    def test_foe_appear_when_roll_die_result_twenty(self, mocked_random_chance):
        expected = True
        actual = game.foe_appear()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_foe_appear_when_roll_die_zero(self, mocked_random_chance):
        expected = True
        actual = game.foe_appear()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=50)
    def test_foe_not_appear_when_roll_die_result_greater_than_twenty(self, mocked_random_chance):
        expected = False
        actual = game.foe_appear()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=21)
    def test_foe_not_appear_when_roll_die_result_twenty_one(self, mocked_random_chance):
        expected = False
        actual = game.foe_appear()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=100)
    def test_foe_not_appear_when_roll_die_result_hundred(self, mocked_random_chance):
        expected = False
        actual = game.foe_appear()
        self.assertEqual(expected, actual)

    def test_output_is_boolean(self):
        foe_appear_chance = game.foe_appear()
        self.assertEqual(type(foe_appear_chance), bool)
