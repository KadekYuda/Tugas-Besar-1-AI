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

    for i in range(len(board)):
        print(board[i])

def compare_heuristic_greater(greater_tuple, lesser_tuple):
    # TODO: Ubah fungsi mengikuti spek
    greater_tuple_val = greater_tuple[0]+greater_tuple[1]
    lesser_tuple_val = lesser_tuple[0]+lesser_tuple[1]
    return greater_tuple_val > lesser_tuple_val