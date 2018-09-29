from random import randint as random


def parse_file(filename):
    '''
    Opens specified input file and parses it
    Outputs a tuple of piece ordering and locations
    '''

    file = open(filename, 'r')

    white_pieces = []
    black_pieces = []

    for line in file:
        color, piece_type, num = line.split()
        num = int(num)

        if color == 'WHITE':
            for i in range(num):
                white_pieces.append(piece_type[0])
        else:
            for i in range(num):
                black_pieces.append(piece_type[0])

    # Assign location to each piece
    white_locs, black_locs = place_pieces(white_pieces, black_pieces)

    return (white_pieces, white_locs, black_pieces, black_locs)

def place_pieces(white, black):
    '''
    Places every pieces (black or white) randomly
    Inputs : list of pieces for each color
    Outputs : location tuples for each color
    '''

    white_locs = []
    black_locs = []

    for i in range(len(white)):
        new_loc = (random(1, 8), random(1, 8))
        while new_loc in white_locs or new_loc in black_locs:
            new_loc = (random(1, 8), random(1, 8))
        white_locs.append(new_loc)

    for i in range(len(black)):
        new_loc = (random(1, 8), random(1, 8))
        while new_loc in white_locs or new_loc in black_locs:
            new_loc = (random(1, 8), random(1, 8))
        black_locs.append(new_loc)

    # Generate random locations for all pieces
    # for i in range(num_black + num_white):
        # new_loc = (random(1, 9), random(1, 9))
        # if new_loc not in locs:
            # locs.append(new_loc)
        # print(locs)

    return (white_locs, black_locs)
