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
    potato = meta_board_maker(lambda: meta_board_maker(Board))
    print(f'Created board has {potato.get_cell_count()} cells')
    if potato.set(2, [3, 3], verbose=True):
        print(potato)
    else:
        print("Fail")