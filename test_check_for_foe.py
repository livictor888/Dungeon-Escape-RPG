import io
from unittest import TestCase
from unittest.mock import patch
from game import check_for_foe
from game import foe_appear


class TestCheckForFoe(TestCase):

    @patch('game.foe_appear', return_value=False)
    def test_healed_when_not_encounter_foe(self, return_value):
        character = dict(hp=20, level=3, level_three_name="Venusaur", exp=250, location=[3, 3], max_hp=30,
                         min_damage=20, max_damage=30)
        boss = dict(hp=30, min_damage=20, max_damage=30, location=[5, 5])
        foe_appear()
        check_for_foe(character, boss)
        actual_hp = character["hp"]
        expected_hp = 24
        self.assertEqual(actual_hp, expected_hp)

    @patch('game.foe_appear', return_value=False)
    def test_return_false_when_not_encounter_foe(self, return_value):
        character = dict(hp=20, level=3, level_three_name="Venusaur", exp=250, location=[3, 3], max_hp=30,
                         min_damage=20, max_damage=30)
        boss = dict(hp=30, min_damage=20, max_damage=30, location=[5, 5])
        foe_appear()
        actual = check_for_foe(character, boss)
        self.assertFalse(actual)

    @patch('builtins.input', side_effect=["no"])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.choice', return_value="Walder")
    @patch('random.randint', side_effect=[50])
    def test_encounter_foe(self, mock_randint, random_foe_name, mock_stdout, mock_input):
        character = dict(hp=20, level=3, level_three_name="Venusaur", exp=250, location=[3, 3], max_hp=30,
                         min_damage=20, max_damage=30)
        boss = dict(hp=30, min_damage=20, max_damage=30, location=[5, 5])
        check_for_foe(character, boss)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = '[Current HP: 24, your Pokemon: Venusaur]\n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('game.foe_appear', return_value=True)
    @patch('builtins.input', side_effect=["no"])
    def test_return_true_when_not_encounter_foe(self, mocked_input, return_value):
        character = dict(hp=20, level=3, level_three_name="Venusaur", exp=250, location=[3, 3], max_hp=30,
                         min_damage=20, max_damage=30)
        boss = dict(hp=30, min_damage=20, max_damage=30, location=[5, 5])
        foe_appear()
        actual = check_for_foe(character, boss)
        self.assertIsNone(actual)
