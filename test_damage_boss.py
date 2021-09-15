from unittest import TestCase
from game import damage_boss


class TestDamageCharacter(TestCase):
    def test_is_boss_alive(self):  # boss takes 12 damage and is still alive
        boss = dict(hp=20, location=[5, 5])
        expect = False
        actual = damage_boss(boss, damage_scale=12)
        self.assertEqual(expect, actual)

    def test_is_boss_dead(self):
        boss = dict(hp=20, location=[5, 5])
        expect = True
        actual = damage_boss(boss, damage_scale=22)
        self.assertEqual(expect, actual)

    def test_is_boss_hp_updated(self):
        boss = dict(hp=20, location=[5, 5])
        damage_boss(boss, damage_scale=12)
        expect = {'hp': 8, 'location': [5, 5]}
        self.assertEqual(expect, boss)

    def test_is_hp_greater_than_zero_when_alive(self):
        boss = dict(hp=20, location=[5, 5])
        damage_boss(boss, damage_scale=12)
        self.assertGreater(boss['hp'], 0)

    def test_is_hp_less_than_or_equal_zero_when_dead(self):
        boss = dict(hp=20, location=[5, 5])
        damage_boss(boss, damage_scale=22)
        self.assertLessEqual(boss['hp'], 0)
