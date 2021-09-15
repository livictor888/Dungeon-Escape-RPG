import io
from unittest import TestCase
from game import win_battle
from unittest.mock import patch


class TestWinBattle(TestCase):
    def test_character_hp_greater_than_zero(self):
        character = dict(hp=20, level=1, exp=250, min_damage=10, max_damage=15,
                         exp_required_to_level=450)
        foe = dict(name="Walder", hp=10, min_damage=10, max_damage=15)
        win_battle(character, foe)
        test_value = character['hp']
        self.assertGreater(test_value, 0)

    def test_foe_hp_equal_less_than_zero(self):
        character = dict(hp=20, level=1, exp=250, min_damage=10, max_damage=15,
                         exp_required_to_level=450)
        foe = dict(name="Walder", hp=0, min_damage=10, max_damage=15)
        win_battle(character, foe)
        test_value = foe['hp']
        self.assertLessEqual(test_value, 0)

    def test_check_level_up_when_reach_required_exp(self):
        character = dict(name='Victor', location=[1, 0], level=1, class_name='Grass', exp=200,
                         level_one_name='Bulbasaur', level_two_name='Ivysaur', level_three_name="Venusaur",
                         hp=40, max_hp=40, hp_growth=20, exp_required_to_level=200,
                         min_damage=10, max_damage=16, damage_growth=5)
        foe = dict(name="Walder", hp=0, min_damage=10, max_damage=15)
        win_battle(character, foe)
        expect_new_level = 2
        actual_new_level = character['level']
        self.assertEqual(expect_new_level, actual_new_level)

    def test_check_new_pokemon_after_levelup(self):
        character = dict(name='Victor', location=[1, 0], level=1, class_name='Grass', exp=200,
                         level_one_name='Bulbasaur', level_two_name='Ivysaur', level_three_name="Venusaur",
                         hp=40, max_hp=40, hp_growth=20, exp_required_to_level=200,
                         min_damage=10, max_damage=16, damage_growth=5)
        foe = dict(name="Walder", hp=0, min_damage=10, max_damage=15)
        win_battle(character, foe)
        expect = 'Ivysaur'
        actual = character['level_two_name']
        self.assertEqual(expect, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_level_up_result_correct(self, mock_stdout):
        character = dict(name='Victor', location=[1, 0], level=1, class_name='Grass', exp=200,
                         level_one_name='Bulbasaur', level_two_name='Ivysaur', level_three_name="Venusaur",
                         hp=40, max_hp=40, hp_growth=20, exp_required_to_level=200,
                         min_damage=10, max_damage=16, damage_growth=5)
        foe = dict(name="Walder", hp=0, min_damage=10, max_damage=15)
        win_battle(character, foe)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = """You gained [92m150[00m exp from this battle!
You leveled up to level 2!
You now deal from 15 to 20 damage!
Your max hp has increased by 20 hp for a total of 60 hp.
Your current Pokemon evolution is Ivysaur.
[Current Status: LEVEL [92m2[00m, [92m150[00m EXP, [92m40[00m HP ]
"""
        self.assertEqual(expected_output, the_game_printed_this)
