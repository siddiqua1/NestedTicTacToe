from board import Board

class Game:
    def __init__(self):
        self.board = self.meta_board_maker(lambda: self.meta_board_maker(lambda: Board()))
        self.player = 1
    
    def __repr__(self) -> str:
        return self.board.__repr__()

    def get_player(self) -> str:
        if self.player == 1:
            return "X"
        elif self.player == 2:
            return "O"
        return "?"

    def get_winner(self) -> int:
        return self.board.value

    def meta_board_maker(self, func) -> Board:
        meta = Board()
        for i in range(9):
            meta.sub_board.append(func())
        return meta

    def cell_to_set(self, cell : int, verbose : bool = False) -> bool:
        if cell > 80 or cell < 0:
            if verbose:
                print(f"Invalid cell {cell}")
            return False
        l1 = cell // 9
        l2 = cell % 9
        res = self.board.set(self.player, [l1, l2], verbose=verbose)
        if res:
            #update player
            self.player = 1 + (self.player)%2 #1 -> 2, 2 -> 1
        return res
    
    def rc_to_set(self, row : int, col : int, verbose : bool = False) -> bool:
        #TODO: this is wrong
        board_num = 3 * (row // 3) + (col // 3)
        board_cell = 3 * (row % 3) + (col % 3)
        return self.cell_to_set(board_num * 9 + board_cell, verbose=verbose)

    def get_valid_moves(self) -> list[int]:
        res = []
        for i, sub in enumerate(self.board.sub_board):
            for j, cell in enumerate(sub.sub_board):
                if cell.value == 0:
                    res.append(9*i + j)
        return res
        
    
    def check_for_reset(self):
        #TODO: after each set, need to check for whether any subboard results in a tie, and if so reset that board
        for i, sub in enumerate(self.board.sub_board):
            
            pass