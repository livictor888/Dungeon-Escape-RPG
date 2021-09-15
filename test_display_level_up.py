from unittest import TestCase
from game import display_level_up
from unittest.mock import patch
import io


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_level_up_to_two(self, print_output):
        character = dict(name='Victor', location=[1, 0], level=2, class_name='Grass', exp=0,
                         level_one_name='Bulbasaur', level_two_name='Ivysaur', level_three_name="Venusaur",
                         hp='40', max_hp='40', hp_growth='20', exp_required_to_level=200,
                         min_damage=10, max_damage=16, damage_growth=5)
        display_level_up(character)
        the_game_printed_this = print_output.getvalue()
        expected_output = "You leveled up to level 2!\nYou now deal from 10 to 15 damage!\n" \
                          "Your max hp has increased by 20 hp for a total of 40 hp.\n" \
                          "Your current Pokemon evolution is Ivysaur.\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_no_evolution_past_level_three(self, print_output):
        character = dict(name='Victor', location=[1, 0], level=4, class_name='Grass', exp=0,
                         level_one_name='Bulbasaur', level_two_name='Ivysaur', level_three_name="Venusaur",
                         hp='40', max_hp='40', hp_growth='20', exp_required_to_level=200,
                         min_damage=10, max_damage=16, damage_growth=5)
        display_level_up(character)
        the_game_printed_this = print_output.getvalue()
        expected_output = "You leveled up to level 4!\nYou now deal from 10 to 15 damage!\n" \
                          "Your max hp has increased by 20 hp for a total of 40 hp.\n" \
                          "Your current Pokemon evolution is Venusaur.\n"
        self.assertEqual(expected_output, the_game_printed_this)
