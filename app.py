from board import Board

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



if __name__ == '__main__':
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
