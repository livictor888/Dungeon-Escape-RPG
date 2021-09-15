from unittest import TestCase
from game import is_boss_alive


class TestIsBossAlive(TestCase):
    def test_boss_hp_greater_than_zero_return_true(self):
        boss = {'hp': 30, 'location': [5, 5]}
        actual = is_boss_alive(boss)
        self.assertTrue(actual)

    def test_boss_hp_equal_zero_return_false(self):
        boss = {'hp': 0, 'location': [5, 5]}
        actual = is_boss_alive(boss)
        self.assertFalse(actual)

    def test_boss_hp_less_than_zero_return_false(self):
        boss = {'hp': -3, 'location': [5, 5]}
        actual = is_boss_alive(boss)
        self.assertFalse(actual)

    def test_return_is_dictionary(self):
        boss = {'hp': 0, 'location': [5, 5]}
        is_boss_alive(boss)
        self.assertIs(type(boss), dict)

    def test_return_True_when_boss_alive(self):
        boss = {'hp': 30, 'location': [5, 5]}
        expect_return_value = is_boss_alive(boss)
        self.assertTrue(expect_return_value)

    def test_return_False_when_boss_hp_equal_zero(self):
        boss = {'hp': 0, 'location': [5, 5]}
        expect_return_value = is_boss_alive(boss)
        self.assertFalse(expect_return_value)

    def test_return_False_when_boss_hp_less_than_zero(self):
        boss = {'hp': -20, 'location': [5, 5]}
        expect_return_value = is_boss_alive(boss)
        self.assertFalse(expect_return_value)

    def test_output_is_boolean(self):
        boss = {'hp': 0, 'location': [5, 5]}
        foe_appear_chance = is_boss_alive(boss)
        self.assertEqual(type(foe_appear_chance), bool)
