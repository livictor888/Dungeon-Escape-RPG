from unittest import TestCase
from game import move
from game import create_board


class TestMove(TestCase):
    def test_move_successfully(self):
        board = create_board()
        character = {"hp": 20, 'level': 1, 'exp': 250, 'location': [3, 3]}
        direction = "1"
        actual_return = move(character, direction, board)
        expected_coordinate = [3, 2]
        expected_return = True
        self.assertEqual(character["location"], expected_coordinate)
        self.assertEqual(actual_return, expected_return)

    def test_try_to_move_out_of_bounds_horizontal_coordinate(self):
        board = create_board()
        character = {"hp": 20, 'level': 1, 'exp': 250, 'location': [24, 5]}
        direction = "4"
        actual_return = move(character, direction, board)
        expected_return = False
        expected_coordinate = [24, 5]
        self.assertEqual(character["location"], expected_coordinate)
        self.assertEqual(actual_return, expected_return)

    def test_try_to_move_out_of_bounds_vertical_coordinate(self):
        board = create_board()
        character = {"hp": 20, 'level': 1, 'exp': 250, 'location': [3, 0]}
        direction = "1"
        actual_return = move(character, direction, board)
        expected_return = False
        expected_coordinate = [3, 0]
        self.assertEqual(character["location"], expected_coordinate)
        self.assertEqual(actual_return, expected_return)

    def test_move_to_edge(self):
        board = create_board()
        character = {"hp": 20, 'level': 1, 'exp': 250, 'location': [23, 24]}
        direction = "4"
        actual_return = move(character, direction, board)
        expected_return = True
        expected_coordinate = [24, 24]
        self.assertEqual(character["location"], expected_coordinate)
        self.assertEqual(actual_return, expected_return)

    def test_bad_input_direction(self):
        board = create_board()
        character = {"hp": 20, 'level': 1, 'exp': 250, 'location': [3, 0]}
        direction = "5"
        actual_return = move(character, direction, board)
        expected_return = False
        expected_coordinate = [3, 0]
        self.assertEqual(character["location"], expected_coordinate)
        self.assertEqual(actual_return, expected_return)
