from board import Board
from game import Game
from random import randint
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
    '''
    basic test to see if board is able to be viewed and interacted with
    '''
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

def print_moves(game):
    print(game)
    print(f"Avaliable moves: {len(game.get_valid_moves())}")

def test2():
    '''
    test to see if ai moves are gotten correctly
    '''
    game = Game()
    print_moves(game)

    game.board.sub_board[8].value = 1
    print_moves(game)

    game.board.sub_board[7].sub_board[0].value = 1
    print_moves(game)
    
    game.board.sub_board[0].value = 2
    print_moves(game)

def test3():
    '''
    test to check if ties reset
    '''
    game = Game()
    game.board.sub_board[0].value = 1
    game.board.sub_board[4].value = 1
    game.board.sub_board[5].value = 1
    game.board.sub_board[6].value = 1

    game.board.sub_board[2].value = 2
    game.board.sub_board[3].value = 2
    game.board.sub_board[7].value = 2
    game.board.sub_board[8].value = 2

    print_moves(game)

    game.board.sub_board[1].sub_board[0].value = 1
    game.board.sub_board[1].sub_board[4].value = 1
    game.board.sub_board[1].sub_board[5].value = 1
    game.board.sub_board[1].sub_board[6].value = 1

    game.board.sub_board[1].sub_board[2].value = 2
    game.board.sub_board[1].sub_board[3].value = 2
    game.board.sub_board[1].sub_board[7].value = 2
    game.board.sub_board[1].sub_board[8].value = 2
    print_moves(game)

    game.cell_to_set(10)
    print_moves(game)

    game.board.sub_board[1].sub_board[0].value = 2
    game.board.sub_board[1].sub_board[1].value = 2
    print_moves(game)

    game.cell_to_set(11)
    print_moves(game)

def AI(move_set : list[int]) -> int:
    return move_set[randint(0, len(move_set) - 1)]

def sanitize_input() -> int:
    try:
        num = int(input())
    except Exception:
        num = -1
    if num > 0 and num < 10:
        return num - 1
    return -1

def player_move(game : Game) -> bool:
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
        return True
    return False

def set_player(player : str) -> bool:
    print(f'Is {player} human? (y/n)')
    buff = ""
    while len(buff) == 0:
        buff = input()
        if buff[0] == "y":
            return True
        if buff[0] == "n":
            return False
        buff = ""

def game_loop():
    game = Game()
    player1 = set_player("Player 1")
    player2 = set_player("Player 2")
    
    while not player1 and not player2:
        print("\nAtleast one player should be human\n")
        player1 = set_player("Player 1")
        player2 = set_player("Player 2")

    while True:
        if game.player == 1:
            if player1:
                player_move(game)
            else:
                cell = AI(game.get_valid_moves())
                game.cell_to_set(cell)
        elif game.player == 2:
            if player2:
                player_move(game)
            else:
                cell = AI(game.get_valid_moves())
                game.cell_to_set(cell)
        
if __name__ == '__main__':
    game_loop()


