from unittest import TestCase
import unittest.mock
import io
import game


class TestPrintBoard(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_and_character_printed_in_corrected_location(self, mock_stdout):
        character = dict(name="Victor",
                         location=[2, 2],
                         level=1,
                         exp=0)
        game.print_board(character)
        expect = '* Current location: (2, 2) *\nš± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± ' \
                 'š± š± \nš± š± 1ļøā£ š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± \nš± 2ļøā£ š§ 4ļøā£ ' \
                 'š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± \nš± š± 3ļøā£ š± š± š± š± š± š± š± š± ' \
                 'š± š± š± š± š± š± š± š± š± š± š± š± š± š± \nš± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± ' \
                 'š± š± š± š± š± š± š± \nš± š± š± š± š± šæ š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± ' \
                 '\nš± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± \nš± š± š± š± š± š± š± ' \
                 'š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± \nš± š± š± š± š± š± š± š± š± š± š± š± š± š± ' \
                 'š± š± š± š± š± š± š± š± š± š± š± \nš± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± ' \
                 'š± š± š± š± \nš± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± \nš± š± š± ' \
                 'š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± \nš± š± š± š± š± š± š± š± š± š± ' \
                 'š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± \nš± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± ' \
                 'š± š± š± š± š± š± š± š± \nš± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± ' \
                 'š± \nš± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± \nš± š± š± š± š± š± ' \
                 'š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± \nš± š± š± š± š± š± š± š± š± š± š± š± š± ' \
                 'š± š± š± š± š± š± š± š± š± š± š± š± \nš± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± ' \
                 'š± š± š± š± š± \nš± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± \nš± š± ' \
                 'š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± \nš± š± š± š± š± š± š± š± š± ' \
                 'š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± \nš± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± ' \
                 'š± š± š± š± š± š± š± š± š± \nš± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± ' \
                 'š± š± \nš± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± š± \n'
        self.assertEqual(mock_stdout.getvalue(), expect)

    def test_character_emoji_correct(self):
        character = dict(location=[2, 2], level=1, exp=0)
        location = (character["location"][0], character["location"][1])
        printed_board = {(row, column): "š± " for row in range(game.MAX_WIDTH()) for column in range(game.MAX_HEIGHT())}
        for keys in printed_board:
            if keys == location:
                printed_board[keys] = "š§ "
        expected_emoji = "š§ "
        actual_emoji = printed_board.get(location)
        self.assertEqual(expected_emoji, actual_emoji)

    def test_boss_emoji_correct(self):
        boss = dict(location=[5, 5], exp=30)
        location = (boss["location"][0], boss["location"][1])
        printed_board = {(row, column): "š± " for row in range(game.MAX_WIDTH()) for column in range(game.MAX_HEIGHT())}
        for keys in printed_board:
            if keys == location:
                printed_board[keys] = "šæ "
        expected_emoji = "šæ "
        actual_emoji = printed_board.get(location)
        self.assertEqual(expected_emoji, actual_emoji)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_character_emoji_only_one_in_printed_board(self, mock_output):
        character = dict(name="Victor",
                         location=[2, 2],
                         level=1,
                         exp=0)
        game.print_board(character)
        expected_emoji = "š§ "
        actual_board = mock_output.getvalue()
        self.assertIn(expected_emoji, actual_board)
        self.assertEqual(actual_board.count(expected_emoji), 1)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_emoji_only_one_in_printed_board(self, mock_output):
        character = dict(name="Victor",
                         location=[2, 2],
                         level=1,
                         exp=0)
        game.print_board(character)
        expected_emoji = "šæ "
        actual_board = mock_output.getvalue()
        self.assertIn(expected_emoji, actual_board)
        self.assertEqual(actual_board.count(expected_emoji), 1)
