from evaluation_function import eval
from parse import place_pieces as generate_position
from parse import parse_file
from util import print_board
from random import uniform
from random import randint


def generate_distribution(frequencies):
    '''
    Creates a probability distribution using given list of frequencies
    with the probability of item with frequency at index i represented
    by a value of the returned list at index i
    '''
    total_frequency = sum(frequencies)

    return [x / total_frequency for x in frequencies]


def distribution_random_choice(pop, distribution, inverse=False):
    '''
    Chooses a random item out of pop with probability for each item as given
    in 'distribution'
    '''

    choice_value = uniform(0, 1)

    if not inverse:
        temp_sum = 0
        for i in range(len(distribution)):
            temp_sum += distribution[i]
            if choice_value <= temp_sum:
                return pop[i]
    else:
        temp_sum = 1
        for i in range(len(distribution)):
            temp_sum -= distribution[i]
            if choice_value >= temp_sum:
                return pop[i]


def crossover(x, y):
    '''
    Crossover two lists of equal length at a random position
    '''
    # Choose a random index as the crossover position
    pos = randint(1, len(x) - 1)

    return (x[:pos] + y[pos:], y[:pos] + x[pos:])


def mutate(l, prob=0.05):
    '''
    Randomly mutate each item within given list 'l'
    '''
    for i in range(len(l)):
        random_chance = uniform(0, 1)
        if random_chance <= prob:
            mutated_position = (randint(1, 8), randint(1, 8))
            while mutated_position in l:
                mutated_position = (randint(1, 8), randint(1, 8))
            l[i] = mutated_position
    return l


def genetic_selection(white, white_pop, black, black_pop, target_pop_size):
    '''
    Generates next generation of population of size 'target_pop_size'
    out of white_pop and black_pop
    '''
    # Evaluate every individual in the population
    costs = []

    for i in range(len(white_pop)):
        black_pos = black_pop[i]
        white_pos = white_pop[i]
        (samecost, diffcost) = eval(black, black_pos, white, white_pos)
        cost = diffcost - samecost
        if cost >= 0:
            costs.append(diffcost - samecost)
        else:
            costs.append(0)

    # Ensure no cost is negative by adding all cost by the smallest negative
    # value + 1(if it exists)
    least_cost = min(costs)
    if least_cost <= 0:
        costs = [x - least_cost + 1 for x in costs]

    # Generate probability distribution for selecting the parents
    distribution = generate_distribution(costs)

    # Select target_pop_size of current population randomly as parents
    # of the next generation
    # Population used in the choosing is a list of indices that represents
    # each individual in the population, because each individual in current
    # population is represented as 2 different lists
    parents = []
    for _ in range(target_pop_size):
        p = distribution_random_choice(range(len(white_pop)), distribution)
        parents.append(p)

    # Do crossover of every pair of parents
    children = []

    for i in range(target_pop_size//2):
        parent1 = white_pop[parents[2 * i]] + black_pop[parents[2 * i + 1]]
        parent2 = white_pop[parents[2 * i]] + black_pop[parents[2 * i + 1]]
        (children1, children2) = crossover(parent1, parent2)
        children.append(children1)
        children.append(children2)

    # Randomly mutate each child
    children = list(map(mutate, children))

    # Split up the children into white and black positions
    white_children = []
    black_children = []
    white_length = len(white_pop[0])
    for i in range(len(children)):
        white_children.append(children[i][:white_length])
        black_children.append(children[i][white_length:])

    return (white_children, black_children)


def genetic(white, black, init_pop=4096, epoc_length=1000):
    '''
    Uses genetic algorithm to calculate the most optimal placement for
    given combination of pieces. Initial population size uses given parameter

    Returns position of black and white pieces
    '''

    white_placements = []
    black_placements = []

    # Generate initial population
    for _ in range(init_pop):
        (white_pos, black_pos) = generate_position(white, black)
        while white_pos in white_placements and black_pos in black_placements:
            (white_pos, black_pos) = generate_position(white, black)
        white_placements.append(white_pos)
        black_placements.append(black_pos)

    # Reduce the population size by half every epoch_length runs
    current_epoch = 0
    target_pop = init_pop
    while target_pop >= 2:
        current_epoch += 1
        # Generate next generation's population
        children = genetic_selection(white, white_placements, black, black_placements, target_pop)
        white_placements = children[0]
        black_placements = children[1]

        if current_epoch == 10:
            current_epoch = 0
            target_pop //= 2

    # If only the final two individuals remain, choose the best between both
    cost1 = eval(black, black_placements[0], white, white_placements[0])
    cost1 = cost1[1] - cost1[0]
    cost2 = eval(black, black_placements[1], white, white_placements[1])
    cost2 = cost2[1] - cost2[0]

    if cost1 >= cost2:
        return (white_placements[0], black_placements[0])
    else:
        return (white_placements[1], black_placements[1])

def genetic_algorithm(input_file, init_pop=4096, epoc_length=1000):
    state = parse_file(input_file)
    genetic_result = genetic(state[0], state[2], init_pop, epoc_length)
    new_state = (state[0], genetic_result[0], state[2], genetic_result[1])
    print_board(new_state)
    print(eval(new_state[2], new_state[3], new_state[0], new_state[1]))
