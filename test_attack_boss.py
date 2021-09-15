import random
from unittest import TestCase
from unittest.mock import patch
from game import attack_boss


class TestAttackBoss(TestCase):
    def test_boss_strike_power_range_correct(self):
        character_speed = 10
        boss_speed = 30
        character = {"hp": 30, 'level': 3, 'exp': 600, 'location': [5, 5], "min_damage": 20, "max_damage": 30}
        boss = {'location': [5, 5], "hp": 30, "min_damage": 20, "max_damage": 30}
        attack_boss(character_speed, boss_speed, character, boss)
        boss_damage = random.randint(boss["min_damage"], boss["max_damage"])
        self.assertGreaterEqual(boss_damage, boss['min_damage'])
        self.assertLessEqual(boss_damage, boss['max_damage'])

    def test_character_strike_power_range_correct(self):
        character_speed = 10
        boss_speed = 30
        character = {"hp": 30, 'level': 3, 'exp': 600, 'location': [5, 5], "min_damage": 20, "max_damage": 30}
        boss = {'location': [5, 5], "hp": 30, "min_damage": 20, "max_damage": 30}
        attack_boss(character_speed, boss_speed, character, boss)
        character_damage = random.randint(boss["min_damage"], boss["max_damage"])
        self.assertGreaterEqual(character_damage, character['min_damage'])
        self.assertLessEqual(character_damage, character['max_damage'])

    @patch('random.randint', side_effect=[15, 15])
    def test_character_hp_update_after_attacked(self, mocked_damage):
        character_speed = 10
        boss_speed = 30
        character = {"hp": 30, 'level': 3, 'exp': 600, 'location': [5, 5], "min_damage": 20, "max_damage": 30}
        boss = {'location': [5, 5], "hp": 30, "min_damage": 20, "max_damage": 30}
        attack_boss(character_speed, boss_speed, character, boss)
        expect = 15
        actual = character['hp']
        self.assertEqual(expect, actual)

    @patch('random.randint', side_effect=[15, 15])
    def test_boss_hp_update_after_attacked(self, mocked_damage):
        character_speed = 30
        boss_speed = 10
        character = {"hp": 30, 'level': 3, 'exp': 600, 'location': [5, 5], "min_damage": 20, "max_damage": 30}
        boss = {'location': [5, 5], "hp": 30, "min_damage": 20, "max_damage": 30}
        attack_boss(character_speed, boss_speed, character, boss)
        expect = 15
        actual = boss['hp']
        self.assertEqual(expect, actual)

    @patch('random.randint', side_effect=[30, 30])
    def test_boss_hp_equal_less_than_zero_when_dead(self, mocked_damage):
        character_speed = 30
        boss_speed = 10
        character = {"hp": 30, 'level': 3, 'exp': 600, 'location': [5, 5], "min_damage": 20, "max_damage": 30}
        boss = {'location': [5, 5], "hp": 30, "min_damage": 20, "max_damage": 30}
        attack_boss(character_speed, boss_speed, character, boss)
        actual = boss['hp']
        self.assertLessEqual(actual, 0)

    @patch('random.randint', side_effect=[30, 30])
    def test_character_hp_equal_less_than_zero_when_dead(self, mocked_damage):
        character_speed = 10
        boss_speed = 30
        character = {"hp": 30, 'level': 3, 'exp': 600, 'location': [5, 5], "min_damage": 20, "max_damage": 30}
        boss = {'location': [5, 5], "hp": 30, "min_damage": 20, "max_damage": 30}
        attack_boss(character_speed, boss_speed, character, boss)
        actual = character['hp']
        self.assertLessEqual(actual, 0)
