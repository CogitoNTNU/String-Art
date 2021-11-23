import numpy as np
import sys


np.set_printoptions(threshold=sys.maxsize)
def crossover(population, top_ratio, bottom_ratio, mutation_rate, pins):
    num_induviduals, lines_plus_one = population.shape
    children = np.zeros((num_induviduals, lines_plus_one), dtype=np.int32)

    top_individuals = int(num_induviduals/top_ratio)
    random_bottom_sample = int(num_induviduals/bottom_ratio)

    # Find best induviduals and place in list
    population_top = population[:top_individuals]
    #print('population_top', population_top.shape)

    # Find worst induviduals
    population_bottom = population[top_individuals:]
    #print('population_bottom', population_bottom.shape)
    # Random sample of worst individuals
    random_indices = np.random.permutation(population_bottom.shape[0])
    random_indices = random_indices[:random_bottom_sample]
    #print('population_bottom.shape[0]', population_bottom.shape[0])
    bottom_sample = population_bottom[random_indices]
    #print('bottom_sample', bottom_sample.shape)

    population_final = np.concatenate((population_top, bottom_sample))
    #print('population', population_final.shape, population_final)

    pop_len = len(population_final)
    random_parents_num = np.random.permutation(pop_len)    
    
    non_mutation_rate = (1-mutation_rate)/2


    for i in range(0, num_induviduals, 2):
        par_one = population_final[random_parents_num[i%pop_len]]
        par_two = population_final[random_parents_num[i%pop_len+1]]
        mutation_pins = np.random.randint(0, pins, size=lines_plus_one)
        #print('mutation_pins', mutation_pins)
        for j in range(lines_plus_one):
            children[i][j] = np.random.choice([par_one[j], par_two[j], mutation_pins[j]], p=[non_mutation_rate, non_mutation_rate, mutation_rate])
            children[i+1][j] = np.random.choice([par_one[j], par_two[j], mutation_pins[j]], p=[non_mutation_rate, non_mutation_rate, mutation_rate])



    #print('children', children.shape, children)
    #print(len(population_final))
    #print(num_induviduals)
    return children

