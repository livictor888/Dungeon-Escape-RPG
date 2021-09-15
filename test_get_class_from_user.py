import io
from unittest import TestCase
from unittest.mock import patch

from game import get_class_from_user


class TestGetClassFromUser(TestCase):

    @patch('builtins.input', side_effect=["7", "hello", "3"])  # 3 invalid inputs
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_if_class_is_invalid(self, mock_stdout, mock_input):
        get_class_from_user()
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = "Invalid input. Try again.\n" \
                          "Invalid input. Try again.\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=["7", "hello", "3", "1"])  # 3 invalid inputs and then 1 valid
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_no_more_invalid_message_after_put_one_valid_input(self, mock_stdout, mock_input):
        get_class_from_user()
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = "Invalid input. Try again.\n" \
                          "Invalid input. Try again.\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=["1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_is_one_when_user_input_one(self, mock_stdout, mock_input):
        actual = get_class_from_user()
        expected_output = '1'
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_is_two_when_user_input_two(self, mock_stdout, mock_input):
        actual = get_class_from_user()
        expected_output = '2'
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["3"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_is_three_when_user_input_three(self, mock_stdout, mock_input):
        actual = get_class_from_user()
        expected_output = '3'
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["4"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_is_four_when_user_input_four(self, mock_stdout, mock_input):
        actual = get_class_from_user()
        expected_output = '4'
        self.assertEqual(expected_output, actual)
