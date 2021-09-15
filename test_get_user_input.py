import io
from unittest import TestCase
from game import get_user_input
from unittest.mock import patch


class TestGetUserInput(TestCase):

    @patch('builtins.input', return_value="hello")
    def test_user_input_other_input_echos(self, mock_input):
        request = "enter anything and get it back"
        actual_return = get_user_input(request)
        expected_return = "hello"
        self.assertEqual(actual_return, expected_return)

    @patch('builtins.input', return_value="some_string")
    def test_user_input_type_string(self, mock_input):
        request = "enter anything and get it back"
        actual_return = get_user_input(request)
        expected_return = str
        self.assertEqual(expected_return, type(actual_return))

    @patch('builtins.input', return_value="list")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_input_is_list(self, mock_stdout, mock_input):
        request = "enter anything and get it back"
        get_user_input(request)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = ("Enter 1 brings you to North\n"
                           "Enter 2 brings you to West\n"
                           "Enter 3 brings you to South\n"
                           "Enter 4 brings you to East\n")
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', return_value="foe")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_input_is_foe(self, mock_stdout, mock_input):
        request = "enter anything and get it back"
        get_user_input(request)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = (
            "[Weevil] : This Pokemon is a grass-type Pokemon and slightly resembles a leopard. It has huge ears, "
            "vine-like fur and a tail full of flowers.\n"
            "[El Nino] : This Pokemon is a fire-type Pokemon and slightly resembles a hedgehog. It has powerful legs, "
            "huge ears and a black snout.\n"
            "[Blast Fungus] : This Pokemon is a ice-type Pokemon and shares features with a termite. It has icy skin, "
            "a fur covered mouth and muscular legs.\n"
            "[Walder] : This Pokemon is a dark-type Pokemon and bears resemblance to an albatross. It has smoke-like "
            "wings, a rugged beak and black and white feathers.\n"
            "[Parasite] : This Pokemon is a bug-type Pokemon and somewhat resembles an ant. It has a little mouth, "
            "thornyskin and ridged legs.\n")
        self.assertEqual(expected_output, the_game_printed_this)
