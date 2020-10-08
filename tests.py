from battleship import BattleshipBoard
import unittest


class TestStringMethods(unittest.TestCase):

    def test_init_board_case_1(self):
        board = BattleshipBoard(5)
        row = ['_']*5
        matrix = []
        for i in range(5):
            matrix.append(row)
        self.assertEqual(board.get_board_status(), matrix)

    def test_update_attacked_position_case_success(self):
        board = BattleshipBoard(5)
        row = ['_'] * 5
        matrix = []
        for i in range(5):
            matrix.append(row)
        board.add_ship_position(0, 1)
        message = board.update_attacked_position(0, 1)
        self.assertEqual(message, 1)

    def test_update_attacked_position_case_missed_target(self):
        board = BattleshipBoard(5)
        row = ['_'] * 5
        matrix = []
        for i in range(5):
            matrix.append(row)
        board.add_ship_position(0, 1)
        message = board.update_attacked_position(1, 1)
        self.assertEqual(message, 0)

    def test_update_attacked_position_case_x_coordinate_out_of_bounds(self):
        board = BattleshipBoard(5)
        row = ['_'] * 5
        matrix = []
        for i in range(5):
            matrix.append(row)
        board.add_ship_position(0, 1)
        message = board.update_attacked_position(10, 10)
        self.assertEqual(message, -1)

    def test_add_ship_position_happy_flow(self):
        board = BattleshipBoard(5)
        row = ['_'] * 5
        matrix = []
        for i in range(5):
            matrix.append(row)
        message = board.add_ship_position(0, 1)
        self.assertEqual(message, 1)

    def test_add_ship_position_already_occupied_coordinate_alive(self):
        board = BattleshipBoard(5)
        row = ['_'] * 5
        matrix = []
        for i in range(5):
            matrix.append(row)
        board.add_ship_position(0, 1)
        message = board.add_ship_position(0, 1)
        self.assertEqual(message, 0)

    def test_add_ship_position_already_occupied_coordinate_dead(self):
        board = BattleshipBoard(5)
        row = ['_'] * 5
        matrix = []
        for i in range(5):
            matrix.append(row)
        board.board[0][1] = 'X'
        message = board.add_ship_position(0, 1)
        self.assertEqual(message, 0)

    def test_add_ship_position_out_of_bounds(self):
        board = BattleshipBoard(5)
        row = ['_'] * 5
        matrix = []
        for i in range(5):
            matrix.append(row)
        message = board.add_ship_position(10, 1)
        self.assertEqual(message, -1)


if __name__ == '__main__':
    unittest.main()
