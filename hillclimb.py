from parse import parse_file
from evaluation_function import eval
from util import print_board, compare_heuristic_greater
import copy

def hillclimb(input_file):
    # membuat current state berupa list apa saja bidak
    current_state = parse_file(input_file)
    # membuat list yang menyimpan current_state board dan nilai heuristik keadaan board
    state_list = [current_state]
    current_heuristic_val = eval(current_state[2],current_state[3],current_state[0],current_state[1])
    max_heuristic_val = current_heuristic_val
    running = True
    #print_board(current_state)
    #print(max_heuristic_val)
    while running:
        new_state = find_next_state(current_state)
        new_state_heuristic_val = eval(new_state[2],new_state[3],new_state[0],new_state[1])
        if compare_heuristic_greater(new_state_heuristic_val, max_heuristic_val):
            current_state = new_state
            max_heuristic_val = new_state_heuristic_val
            state_list.append(current_state)
        else:
            running = False
    print_board(current_state)
    print(max_heuristic_val)

def find_next_state(current_state):
    # mencari state selanjutnya dari board
    # state yang dicari adalah state terbaik yang didapat dari pemindahan satu piece yang memberikan heuristik terbaik
    new_state = copy.deepcopy(current_state)
    test_state = copy.deepcopy(current_state)
    max_heuristic_val = eval(current_state[2],current_state[3],current_state[0],current_state[1])
    # memeriksa piece putih bisa dipindahkan ke mana saja yang paling efektif
    for idx in range(len(current_state[1])):
        for i in range(1,9):
            for j in range(1,9):
                testing_place = (i,j)
                if not(testing_place in test_state[1]) and not(testing_place in test_state[3]):
                    #print(test_state)
                    test_state[1].pop(idx)
                    test_state[1].insert(idx, testing_place)
                    test_heuristic_val = eval(test_state[2], test_state[3], test_state[0], test_state[1])
                    if compare_heuristic_greater(test_heuristic_val, max_heuristic_val):
                        new_state = copy.deepcopy(test_state)
                        max_heuristic_val = test_heuristic_val
        test_state = copy.deepcopy(current_state)
    
    for idx in range(len(current_state[3])):
        for i in range(1,9):
            for j in range(1,9):
                testing_place = (i,j)
                if not(testing_place in test_state[1]) and not(testing_place in test_state[3]):
                    #print(test_state)
                    test_state[3].pop(idx)
                    test_state[3].insert(idx, testing_place)
                    test_heuristic_val = eval(test_state[2], test_state[3], test_state[0], test_state[1])
                    if compare_heuristic_greater(test_heuristic_val, max_heuristic_val):
                        new_state = copy.deepcopy(test_state)
                        max_heuristic_val = test_heuristic_val
        test_state = copy.deepcopy(current_state)

    return new_state

if __name__ == "__main__":
    hillclimb("input.txt")