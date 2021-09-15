from unittest import TestCase
from game import damage_character


class TestDamageCharacter(TestCase):
    def test_is_character_alive(self):
        character = {'hp': 20, 'location': [2, 4]}
        expect = False
        actual = damage_character(character, damage_scale=12)
        self.assertEqual(expect, actual)

    def test_is_character_dead(self):
        character = {'hp': 20, 'location': [2, 4]}
        expect = True
        actual = damage_character(character, damage_scale=22)
        self.assertEqual(expect, actual)

    def test_is_character_hp_updated(self):
        character = {'hp': 20, 'location': [2, 4]}
        damage_character(character, damage_scale=12)
        expect = {'hp': 8, 'location': [2, 4]}
        actual = character
        self.assertEqual(expect, actual)

    def test_is_hp_greater_than_zero_when_alive(self):
        character = {'hp': 20, 'location': [2, 4]}
        damage_character(character, damage_scale=12)
        self.assertGreater(character['hp'], 0)

    def test_is_hp_less_than_zero_when_dead(self):
        character = {'hp': 20, 'location': [2, 4]}
        damage_character(character, damage_scale=22)
        self.assertLess(character['hp'], 0)

    def test_is_hp_equal_zero_when_dead(self):
        character = {"hp": 20, 'location': [2, 4]}
        damage_character(character, damage_scale=20)
        self.assertEqual(character['hp'], 0)
