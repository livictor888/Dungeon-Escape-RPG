from unittest import TestCase
from game import create_boss


class TestCreateBoss(TestCase):
    def test_return_is_dictionary(self):
        boss = create_boss()
        self.assertIs(type(boss), dict)

    def test_boss_location_is_correct(self):
        boss = create_boss()
        actual = boss['location']
        expect = [5, 5]
        self.assertEqual(expect, actual)

    def test_boss_contains_all_correct_keys(self):
        boss = create_boss()
        self.assertIn("hp", boss)
        self.assertIn("min_damage", boss)
        self.assertIn("max_damage", boss)
        self.assertIn("location", boss)

    def test_boss_ability_correct(self):
        boss = create_boss()
        expected_hp = 80
        expected_min_damage = 15
        expected_max_damage = 20
        self.assertEqual(expected_hp, boss['hp'])
        self.assertEqual(expected_min_damage, boss['min_damage'])
        self.assertEqual(expected_max_damage, boss['max_damage'])
