from unittest import TestCase
from game import damage_foe


class TestDamageFoe(TestCase):
    def test_foe_alive(self):
        foe = {'hp': 20, 'location': [4, 5]}
        expect = False
        actual = damage_foe(foe, damage_scale=12)
        self.assertEqual(expect, actual)

    def test_foe_dead(self):
        foe = {'hp': 20, 'location': [4, 5]}
        expect = True
        actual = damage_foe(foe, damage_scale=22)
        self.assertEqual(expect, actual)

    def test_foe_hp_updated_correct(self):
        foe = {'hp': 20, 'location': [4, 5]}
        damage_foe(foe, damage_scale=12)
        expect = {'hp': 8, 'location': [4, 5]}
        actual = foe
        self.assertEqual(expect, actual)

    def test_is_hp_greater_than_zero_when_alive(self):
        foe = {'hp': 20, 'location': [4, 5]}
        damage_foe(foe, damage_scale=12)
        self.assertGreater(foe['hp'], 0)

    def test_is_hp_less_than_zero_when_dead(self):
        foe = {'hp': 20, 'location': [4, 5]}
        damage_foe(foe, damage_scale=22)
        self.assertLess(foe['hp'], 0)

    def test_is_hp_equal_zero_when_dead(self):
        foe = {'hp': 20, 'location': [4, 5]}
        damage_foe(foe, damage_scale=20)
        self.assertEqual(foe['hp'], 0)
