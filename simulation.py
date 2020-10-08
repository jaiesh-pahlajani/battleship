from battleship import BattleshipBoard
from player import Player


M = int(input())
if M < 0 or M > 9:
    raise Exception('Invalid Size')

board = BattleshipBoard(M)

S = int(input())
if S > M*M:
    raise Exception('Invalid Number of ships')

board.init_total_number_of_ships(S)

ship_position_str = input()
# validation for ship positions
ship_position_list = ship_position_str.split(':')
if len(ship_position_list) < S:
    raise Exception('Not all positions for ship are specified')
if len(ship_position_list) > S:
    raise Exception('Excess positions specified')

for position in ship_position_list:
    pair = position.split(',')
    board.add_ship_position(int(pair[0]), int(pair[1]))

T = int(input())
if T > M*M:
    raise Exception('Invalid Number of missiles')


missile_position_str = input()
# Set Missile positions for player

missile_position_list = missile_position_str.split(':')
if len(missile_position_list) < S:
    raise Exception('Not all positions for missile are specified')
if len(missile_position_list) > S:
    raise Exception('Excess actions specified')

player = Player(T)
# player2 = Player(N)
player.init_missile_positions(missile_position_list)
player.attack(board)
# player.attack(board)

print(board.get_board_status())
