from parse import parse_file, place_pieces
from evaluation_function import eval
from util import print_board, compare_heuristic_greater, find_next_state
import copy
import math
import random

def update_temperature(T):
    return T*(1-0.3)

def acceptance_probabilty(temperature, delta):
	x = delta / temperature
	p = math.exp(x)
	r = random.random()
	return (r < p)

def delta(current_state_heuristic, next_state_heuristic):
    return (current_state_heuristic[1] - current_state_heuristic[0]) - (next_state_heuristic[1] - next_state_heuristic [0])

def simulated_annealing(input_file):
	current_state = parse_file(input_file)
	state_list = [current_state]
	current_heuristic_val = eval(current_state[2],current_state[3],current_state[0],current_state[1])
	max_state = current_state
	max_heuristic_val = current_heuristic_val
	T = 100000
	while (T > 0.1):
		new_state = find_next_state(current_state)
		new_state_heuristic_val = eval(new_state[2],new_state[3],new_state[0],new_state[1])
		d = delta(current_heuristic_val, new_state_heuristic_val)
		if d > 0:
			current_state = new_state
			current_heuristic_val = new_state_heuristic_val
			state_list.append(current_state)
		else:
			if (acceptance_probabilty(T,d)):
				current_state = new_state
				current_heuristic_val = new_state_heuristic_val
				state_list.append(current_state)
		
		if (compare_heuristic_greater(current_heuristic_val,max_heuristic_val)):
			max_heuristic_val = current_heuristic_val
			max_state = current_state

		T = update_temperature(T)

	print_board(max_state)
	print(max_heuristic_val)

if __name__ == "__main__":
    simulated_annealing("input.txt")