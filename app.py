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

if __name__ == '__main__':
    potato = Board()
    if potato.set(4, 2, verbose=True):
        print(potato)
    else:
        print("Fail")