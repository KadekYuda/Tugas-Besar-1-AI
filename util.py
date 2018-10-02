from copy import deepcopy
from evaluation_function import eval

def print_board(piece_list):
    """
        Mencetak board sesuai dari informasi yang ada dari board list.

        Parameter:
            piece_list: List yang berisi informasi soal piece putih dan hitam beserta lokasinya.
    """
    whitepieces = piece_list[0]
    whitepos = piece_list[1]
    blackpieces = piece_list[2]
    blackpos = piece_list[3]
    # inisiasi board kosong 8x8, sesuai ukuran papan catur
    board = [['*' for i in range(8)] for i in range(8)]
    
    # meletakkan white piece pada posisinya
    for i in range(len(whitepos)):
        wpos = whitepos[i]
        wpiece = whitepieces[i]
        board[wpos[0]-1][wpos[1]-1] = wpiece

    # meletakkan black piece pada posisinya
    for i in range(len(blackpos)):
        bpos = blackpos[i]
        bpiece = blackpieces[i].lower()
        board[bpos[0]-1][bpos[1]-1] = bpiece

    for row in board:
        for column in row:
            print(column, end ='')
        print()

def compare_heuristic_greater(greater_tuple, lesser_tuple):
    return (greater_tuple[1] - greater_tuple [0]) > (lesser_tuple[1] - lesser_tuple[0])


def find_next_state(current_state):
    '''
    mencari state selanjutnya dari board
    state yang dicari adalah state terbaik yang didapat dari pemindahan satu piece yang memberikan heuristik terbaik
    '''
    new_state = deepcopy(current_state)
    test_state = deepcopy(current_state)
    max_heuristic_val = eval(current_state[2],current_state[3],current_state[0],current_state[1])
    # memeriksa piece putih bisa dipindahkan ke mana saja yang paling efektif
    for idx in range(len(current_state[1])):
        for i in range(1,9):
            for j in range(1,9):
                testing_place = (i,j)
                if not(testing_place in test_state[1]) and not(testing_place in test_state[3]):
                    test_state[1].pop(idx)
                    test_state[1].insert(idx, testing_place)
                    test_heuristic_val = eval(test_state[2], test_state[3], test_state[0], test_state[1])
                    if compare_heuristic_greater(test_heuristic_val, max_heuristic_val):
                        new_state = deepcopy(test_state)
                        max_heuristic_val = test_heuristic_val
        test_state = deepcopy(current_state)
    
    # memeriksa piece hitam bisa dipindahkan ke mana saja yang paling efektif
    for idx in range(len(current_state[3])):
        for i in range(1,9):
            for j in range(1,9):
                testing_place = (i,j)
                if not(testing_place in test_state[1]) and not(testing_place in test_state[3]):
                    test_state[3].pop(idx)
                    test_state[3].insert(idx, testing_place)
                    test_heuristic_val = eval(test_state[2], test_state[3], test_state[0], test_state[1])
                    if compare_heuristic_greater(test_heuristic_val, max_heuristic_val):
                        new_state = deepcopy(test_state)
                        max_heuristic_val = test_heuristic_val
        test_state = deepcopy(current_state)

    return new_state