class Board:

    int_to_str = {0 : "*", 1 : "X", 2 : "O"}

    def __init__(self):
        self.value : int = 0
        self.sub_board : list[Board] = []

    def reset(self):
        self.value = 0
        for board in self.sub_board:
            board.reset()

    def set(self, value : int, loc : list[int], verbose : bool = False) -> bool:
        if value > 3 or value < 0:
            return False
        if len(loc) == 0:
            if not self.sub_board:
                self.value = value
                return True
            return False
        res = self.sub_board[loc[0]].set(value, loc[1:], verbose=verbose)
        if res:
            self.winner_update()
        return res

    def rec_board_builder(self, factor = 3) -> list[int]:
        builder = []
        if not self.sub_board:
            builder.append(self.int_to_str.get(self.value, "?")) 
            return builder
        for sub in self.sub_board:
            builder = builder + sub.rec_board_builder()
        

        if self.value != 0:
            tmp = ['-' for i in range(len(builder))]
            tmp[int(len(builder)//2) ] = self.int_to_str.get(self.value, "?")
            builder = tmp
        else: 
            #rearrange
            n = int(len(builder) / (factor*factor))
            row_number = int(n**0.5)
            if row_number == 0:
                return builder
            tmp2 = []
            #print(f'row_number: {row_number} n: {n}')
            for r in range(factor):
                for rr in range(row_number):
                    for c in range(factor):
                        row_start = (r*n*factor + c*n + rr * int(n**0.5))
                        tmp2 += builder[row_start:row_start+row_number]
            builder = tmp2
        return builder

    def winner_update(self):
        pass

    def get_cell_count(self) -> int:
        b = self.rec_board_builder()
        return len(b)

    def get_depth(self) -> int:
        '''
        Assumes that the board is constructed evenly
        '''
        if not self.sub_board:
            return 0
        return 1 + self.sub_board[0].get_depth()

    def __repr__(self, board_factor = 3) -> str:
        b = self.rec_board_builder()
        #TODO: Rearrange better
        rt = int(len(b)**0.5)
        if len(b) == rt*rt:
            for i in range(rt):
                b.insert(i * (rt + 1), "\n")
        return " ".join(b)