class Board:
    '''
    Board for one instance of tic tac toe
    '''

    def __init__(self):
        self.tiles = [0 for i in range(9)]
        self.resolved = False
        self.winner = 0

    def reset(self):
        '''
        Resets the board to its original state
        '''
        self.tiles = [0 for i in range(9)]
        self.winner = 0

    def set(self, loc, cell, verbose = False) -> bool:
        '''
        Function that sets a location on a board to belong to the player passed in.
        Returns `False` when failing to do so.
        '''
        if self.winner != 0:
            if verbose:
                print("[Failed to set] Board is resolved")
            return False
        if loc < 0 or loc > 8:
            if verbose:
                print(f"[Failed to set] Location {loc} is not in bounds")
            return False
        if self.tiles[loc] != 0:
            if verbose:
                print(f"[Failed to set] Location {loc} is already set to {self.tiles[loc]}")
            return False
        if cell != 1 and cell != 2:
            if verbose:
                print(f"[Failed to set] Value {cell} is not a valid player")
            return False
        self.tiles[loc] = cell
        self.update_for_winner()
        return True

    def update_for_winner(self):
        '''
        Updates the board to see if anyone won the game
        '''
        


    def tile_to_string(self, tile):
        if tile == 0:
            return " "
        elif tile == 1:
            return "X"
        elif tile == 2:
            return "O"
        return tile.winner
        
    def __repr__(self):
        sb = []
        for i, tile in enumerate(self.tiles):
            if i % 3 != 2:
                sb.append(f' {self.tile_to_string(tile)} |')
            else:
                if i == 8:
                    sb.append(f' {self.tile_to_string(tile)} \n')
                else:
                    sb.append(f' {self.tile_to_string(tile)} \n-----------\n')
        return ''.join(sb)
