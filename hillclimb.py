from parse import parse_file
from evaluation_function import eval
from util import print_board, compare_heuristic_greater, find_next_state
import copy

def hillclimb(input_file):
    '''
    Menggunakan algoritma Hill-Climbing untuk mencari kombinasi optimal
    jika diberikan bidaknya.

    Parameter: input_file (str)

    Mencetak board yang sudah diselesaikan.
    '''
    # membuat current state berupa list apa saja bidak
    current_state = parse_file(input_file)
    # membuat list yang menyimpan current_state board dan nilai heuristik keadaan board
    max_heuristic_val = eval(current_state[2],current_state[3],current_state[0],current_state[1])
    running = True
    while running:
        new_state = find_next_state(current_state)
        new_state_heuristic_val = eval(new_state[2],new_state[3],new_state[0],new_state[1])
        if compare_heuristic_greater(new_state_heuristic_val, max_heuristic_val):
            current_state = new_state
            max_heuristic_val = new_state_heuristic_val
        else:
            running = False
    print_board(current_state)
    print(max_heuristic_val)

if __name__ == "__main__":
    hillclimb("input.txt")