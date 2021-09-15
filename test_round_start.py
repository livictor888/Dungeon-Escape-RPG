import io
from unittest import TestCase
from unittest.mock import patch

from game import round_start, roll_die
import random


class TestRoundStart(TestCase):

    def test_chance_of_foe_flee_correct(self):
        number_of_roll = 10000000
        percentage_of_foe_flee = 20
        result = [random.randint(1, 5) for _ in range(number_of_roll)]
        number_for_foe_flee = []
        for i in result:
            if i <= 1:
                number_for_foe_flee.append(i)
        expected_chance = percentage_of_foe_flee
        actual_chance = len(number_for_foe_flee) * 100 / number_of_roll
        self.assertAlmostEqual(expected_chance, actual_chance, 1)

    @patch('random.randint', side_effect=[30, 15, 3, 40, 10, 10, 30])
    @patch('builtins.input', side_effect=["no"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_strike_first_when_win_roll_die(self, mock_stdout, mock_input, mock_randint):
        character = dict(hp=20, level=1, exp=250, min_damage=10, max_damage=15,
                         exp_required_to_level=450)
        foe = dict(name="Walder", hp=10, min_damage=10, max_damage=15)
        action = "k"
        round_start(character, foe, action)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = """You attacked Walder. The demon lost 10 HP
[1;35mThe Walder has been defeated[0m
You gained [92m150[00m exp from this battle!
[Current Status: LEVEL [92m1[00m, [92m400[00m EXP, [92m20[00m HP ]
"""
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', side_effect=[15, 30, 3, 10, 10, 30, 15, 3, 10, 10])
    @patch('builtins.input', side_effect=["no"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_foe_strike_first_when_win_roll_die(self, mock_stdout, mock_input, mock_randint):
        character = dict(hp=20, level=1, exp=250, min_damage=10, max_damage=15,
                         exp_required_to_level=450)
        foe = dict(name="Walder", hp=10, min_damage=10, max_damage=15)
        action = "k"
        round_start(character, foe, action)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = """The Walder attacked you. You lost 10 HP
[Current Status: LEVEL [92m1[00m, [92m250[00m EXP, [92m10[00m HP ]
You attacked Walder. The demon lost 10 HP
[1;35mThe Walder has been defeated[0m
You gained [92m150[00m exp from this battle!
[Current Status: LEVEL [92m1[00m, [92m400[00m EXP, [92m10[00m HP ]
"""
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=["no"])
    def test_if_character_speed_positive_int(self, mock_input):
        character = dict(hp=20, level=1, exp=250, min_damage=10, max_damage=15,
                         exp_required_to_level=450)
        foe = dict(name="Walder", hp=10, min_damage=10, max_damage=15)
        action = 'no'
        round_start(character, foe, action)
        character_speed = roll_die()
        actual = character_speed
        self.assertEqual(int, type(actual))
        self.assertGreater(actual, 0)

    @patch('builtins.input', side_effect=["no"])
    def test_if_foe_speed_positive_int(self, mock_input):
        character = dict(hp=20, level=1, exp=250, min_damage=10, max_damage=15,
                         exp_required_to_level=450)
        foe = dict(name="Walder", hp=10, min_damage=10, max_damage=15)
        action = 'no'
        round_start(character, foe, action)
        foe_speed = roll_die()
        actual = foe_speed
        self.assertEqual(int, type(actual))
        self.assertGreater(actual, 0)
