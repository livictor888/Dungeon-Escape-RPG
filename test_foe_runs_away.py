import io
from unittest import TestCase
from unittest.mock import patch

from game import foe_runs_away


class TestFoeRunsAway(TestCase):
    def test_if_character_hp_greater_than_zero(self):
        character = {'level': 1, 'exp': 150, 'hp': 20, 'location': [2, 4]}
        foe = {'name': 'Walder', 'hp': 30, 'location': [2, 4]}
        foe_runs_away(character, foe)
        expect = character['hp']
        self.assertGreater(expect, 0)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_runs_way_message(self, mock_stdout):
        character = {'level': 1, 'exp': 150, 'hp': 20, 'location': [2, 4]}
        foe = {'name': 'Walder', 'hp': 30, 'location': [2, 4]}
        foe_runs_away(character, foe)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = 'Walder ran away!!!\n[Current Status: LEVEL [92m1[00m, [92m150[00m EXP[92m20[00m HP ]\n'
        self.assertEqual(expected_output, the_game_printed_this)

    def test_character_hp_not_change_when_foe_fleeing(self):
        character = {'level': 1, 'exp': 150, 'hp': 20, 'location': [2, 4]}
        foe = {'name': 'Walder', 'hp': 30, 'location': [2, 4]}
        foe_runs_away(character, foe)
        expect = 20
        self.assertEqual(expect, character['hp'])

    def test_character_hp_positive_integer(self):
        character = {'level': 1, 'exp': 150, 'hp': 20, 'location': [2, 4]}
        foe = {'name': 'Walder', 'hp': 30, 'location': [2, 4]}
        foe_runs_away(character, foe)
        self.assertGreater(character['hp'], 0)
        self.assertEqual(int, type(character['hp']))
