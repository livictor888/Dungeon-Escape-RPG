from unittest import TestCase
from game import check_for_boss


class TestCheckForBoss(TestCase):

    def test_boss_character_location_same(self):
        character = {'location': [5, 5], 'min_damage': 20, 'max_damage': 25, 'hp': 20, 'level': 1, 'exp': 0}
        boss = {'location': [5, 5], 'hp': 30, 'min_damage': 20, 'max_damage': 30}
        check_for_boss(character, boss)
        self.assertEqual(character['location'], boss['location'])

    def test_return_true_when_meet_boss(self):
        character = {'location': [5, 5], 'min_damage': 20, 'max_damage': 25, 'hp': 20, 'level': 1, 'exp': 0}
        boss = {'location': [5, 5], 'hp': 30, 'min_damage': 20, 'max_damage': 30}
        expect = check_for_boss(character, boss)
        self.assertTrue(expect)

    def test_return_false_not_meet_boss(self):
        character = {'location': [3, 2], 'min_damage': 20, 'max_damage': 25, 'hp': 20, 'level': 1, 'exp': 0}
        boss = {'location': [5, 5], 'hp': 30, 'min_damage': 20, 'max_damage': 30}
        expect = check_for_boss(character, boss)
        self.assertFalse(expect)

    def test_boss_location_is_correct(self):
        character = {'location': [3, 2], 'min_damage': 20, 'max_damage': 25, 'hp': 20, 'level': 1, 'exp': 0}
        boss = {'location': [5, 5], 'hp': 30, 'min_damage': 20, 'max_damage': 30}
        actual = boss['location']
        check_for_boss(character, boss)
        expect = [5, 5]
        self.assertEqual(expect, actual)

    def test_character_hp_greater_than_zero(self):
        character = {'location': [3, 2], 'min_damage': 20, 'max_damage': 25, 'hp': 20, 'level': 1, 'exp': 0}
        boss = {'location': [5, 5], 'hp': 30, 'min_damage': 20, 'max_damage': 30}
        check_for_boss(character, boss)
        actual = boss['location']
        expect = [5, 5]
        self.assertEqual(expect, actual)
