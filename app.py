from board import Board
from game import Game
'''
Ideation:
since this is a meta game maybe itll be cleaner to define a object board that has 
pointer(s) to sub boards

like a linked list is defined as a value and a pointer to the next linked list

Specs
init(num_tiles):
    winner #decides what the value of the meta board is
    actual tiles 
    


'''

def reg_board_maker() -> Board:
    big = Board()
    for i in range(9):
        big.sub_board.append(Board())
    return big

def meta_board_maker(func) -> Board:
    meta = Board()
    for i in range(9):
        meta.sub_board.append(func())
    return meta


def test():
    potato = Board()
    potato = meta_board_maker(lambda: Board())
    potato = meta_board_maker(lambda: meta_board_maker(lambda: Board()))
    #potato = meta_board_maker(lambda: meta_board_maker(lambda: meta_board_maker(Board)))
    #potato.sub_board[7].value = 1
    #potato.sub_board[5].value = 1
    #potato.sub_board[8].sub_board[1].value = 2
    print(f'Created board has {potato.get_cell_count()} cells')
    #print(potato)
    for r in range(3, 6):
        for c in range (3,6):
            if potato.set(2, [r, c], verbose=True):
                print(potato)
            else:
                print("Fail")

def sanitize_input() -> int:
    try:
        num = int(input())
    except Exception:
        num = -1
    if num > 0 and num < 10:
        return num - 1
    return -1

def game_loop():
    game = Game()
    while True:
        print(game)
        print(f"\nIt is player {game.get_player()}'s turn.\n")
        
        row = -1
        while row == -1:
            print(f"Input row (1-9): ")
            row = sanitize_input()
            print()
        col = -1
        while col == -1:
            print(f"Input col (1-9): ")
            col = sanitize_input()
            print()
        res = game.rc_to_set(row, col)
        if not res:
            print(f"Player {game.get_player()}'s move is invalid, try again")
        
        if game.get_winner() > 0:
            player = "X" if game.get_winner() == 1 else "O"
            print(f"Player {player} has won the game!")
            break

if __name__ == '__main__':
    game_loop()
