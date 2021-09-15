from unittest import TestCase
import game


class TestLevelUp(TestCase):

    def test_correct_exp_gain(self):
        actual_character = dict(name='Victor', location=[1, 0], level=1, class_name='Grass', exp=0,
                                level_one_name='Bulbasaur', level_two_name='Ivysaur', level_three_name="Venusaur",
                                hp=40, max_hp=40, hp_growth=20, exp_required_to_level=200,
                                min_damage=10, max_damage=16, damage_growth=5)
        game.level_up(actual_character)
        expected_exp = 150
        self.assertEqual(expected_exp, actual_character['exp'])

    def test_added_damage_correct_after_level_up(self):
        actual_character = dict(level=1, exp=200, level_two_name='Ivysaur',
                                hp=40, max_hp=40, hp_growth=20, exp_required_to_level=200,
                                min_damage=10, max_damage=16, damage_growth=5)
        game.level_up(actual_character)
        expected_min_damage_after_leveling = 15
        expected_max_damage_after_leveling = 21
        self.assertEqual(actual_character['min_damage'], expected_min_damage_after_leveling)
        self.assertEqual(actual_character['max_damage'], expected_max_damage_after_leveling)

    def test_added_hp_correct_after_level_up(self):
        actual_character = dict(name='Victor', location=[1, 0], level=1, class_name='Grass', exp=200,
                                level_one_name='Bulbasaur', level_two_name='Ivysaur', level_three_name="Venusaur",
                                hp=40, max_hp=40, hp_growth=20, exp_required_to_level=200,
                                min_damage=10, max_damage=16, damage_growth=5)
        game.level_up(actual_character)
        expected_hp = 40
        self.assertEqual(expected_hp, actual_character['hp'])

    def test_is_level_updated_correct_after_level_up(self):
        actual_character = dict(level=1, class_name='Grass', exp=200, level_two_name='Ivysaur',
                                hp=40, max_hp=40, hp_growth=20, exp_required_to_level=200,
                                min_damage=10, max_damage=16, damage_growth=5)
        game.level_up(actual_character)
        expected_level = 2
        self.assertEqual(actual_character['level'], expected_level)

    def test_is_pokemon_evolved_correct_after_level_up(self):
        actual_character = dict(level=1, class_name='Grass', exp=200,
                                level_one_name='Bulbasaur', level_two_name='Ivysaur', level_three_name="Venusaur",
                                hp=40, max_hp=40, hp_growth=20, exp_required_to_level=200,
                                min_damage=10, max_damage=16, damage_growth=5)
        game.level_up(actual_character)
        expected_pokemon = 'Ivysaur'
        self.assertEqual(actual_character['level_two_name'], expected_pokemon)

    def test_pokemon_does_not_evolve_past_level_3(self):  # past level 3 Pokemon doesn't evolve
        actual_character = dict(level=3, exp=500, level_three_name="Venusaur",
                                hp=40, max_hp=40, hp_growth=20, exp_required_to_level=200,
                                min_damage=10, max_damage=16, damage_growth=5)
        game.level_up(actual_character)
        expected_evolution = "Venusaur"
        self.assertEqual(actual_character['level_three_name'], expected_evolution)
