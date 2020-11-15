class Player:

    def __init__(self, total_number_of_missiles):
        self.total_number_of_missiles = total_number_of_missiles
        self.missile_positions_str = 0
        self.missile_positions_list = []

    def init_missile_positions(self, missile_positions_list):
        """

        :param missile_positions_list: This is a list of input missile pos [[0,1],[1,2]]
        """
        self.missile_positions_list = missile_positions_list

    def attack(self, board):
        for missile in self.missile_positions_list:
            pair = missile.split(',')
            board.update_attacked_position(int(pair[0]), int(pair[1]))
