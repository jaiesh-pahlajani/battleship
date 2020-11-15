
class PositionRepresentation:
    DEFAULT = '_'
    ALIVE = 'B'
    DEAD_SHIP = 'X'
    MISSED = 'O'


class BattleshipBoard:

    def __init__(self, size_of_board):

        self.size_of_board = size_of_board
        self.board = []
        for i in range(self.size_of_board):
            self.board.append([PositionRepresentation.DEFAULT]*self.size_of_board)
        self.total_number_of_ships = 0

    def init_total_number_of_ships(self, total_number_of_ships):
        self.total_number_of_ships = total_number_of_ships

    def add_ship_position(self, x_coordinate, y_coordinate):
        if x_coordinate > len(self.board) or y_coordinate > len(self.board[0]):
            return -1

        if self.board[x_coordinate][y_coordinate] == PositionRepresentation.DEFAULT:
            self.board[x_coordinate][y_coordinate] = PositionRepresentation.ALIVE
            return 1
        else:
            return 0

    def update_attacked_position(self, x_coordinate, y_coordinate):

        if x_coordinate > len(self.board) or y_coordinate > len(self.board[0]):
            return -1

        if self.board[x_coordinate][y_coordinate] == PositionRepresentation.DEFAULT:
            self.board[x_coordinate][y_coordinate] = PositionRepresentation.MISSED
            message = 0
        else:
            self.board[x_coordinate][y_coordinate] = PositionRepresentation.DEAD_SHIP
            message = 1

        return message

    def get_board_status(self):
        return self.board
