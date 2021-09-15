from unittest import TestCase

from game import heal
from game import HEALING_RATE


class TestHeal(TestCase):

    def test_character_hp_updated_correct_after_healed(self):
        character = {"hp": 10, "max_hp": 20}
        heal(character)
        actual = character
        expected = {"hp": 14, "max_hp": 20}
        self.assertEqual(actual, expected)

    def test_healing_character_never_exceed_max_hp(self):
        character = {"hp": 18, "max_hp": 20}
        heal(character)
        actual = character
        expected = {"hp": 20, "max_hp": 20}
        self.assertEqual(actual, expected)

    def test_no_hp_change_if_already_reach_max_hp_after_heal(self):
        character = {"hp": 20, "max_hp": 20}
        heal(character)
        actual = character
        expected = {"hp": 20, "max_hp": 20}
        self.assertEqual(actual, expected)

    def test_healed_hp_same_as_healing_rate(self):
        character = {"hp": 10, "max_hp": 20}
        original_hp = 10
        healing_rate = HEALING_RATE()
        heal(character)
        expect = character['hp'] - original_hp
        self.assertEqual(expect, healing_rate)