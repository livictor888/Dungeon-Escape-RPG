from unittest import TestCase
from unittest.mock import patch

import game


class TestRollDie(TestCase):
    def test_roll_die_value_correct(self):
        roll_die_result = game.roll_die()
        self.assertLess(roll_die_result, 100)
        self.assertGreater(roll_die_result, 1)

    def test_result_is_integer(self):
        roll_die_result = game.roll_die()
        self.assertTrue(type(roll_die_result) is int)

    @patch('random.randint', side_effect=[5])
    def test_roll_die_single_time(self, mock_randint):
        actual = game.roll_die()
        self.assertEqual(actual, 5)




