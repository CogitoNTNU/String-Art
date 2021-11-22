import numpy as np

'''
pins = 256
num_induviduals = 1024
lines = 12
population1 = np.random.randint(0, pins, size=(num_induviduals,lines+1))
population2 = np.random.randint(0, pins, size=(num_induviduals,lines+1))
population1_fit = np.random.rand(1,num_induviduals)
population2_fit = np.random.rand(1,num_induviduals)
'''

def selection(population_one, population_two, population_one_fitness, population_two_fitness):

    top_individuals = int(population_one.shape[0]/2)
    random_bottom_sample = int(population_one.shape[0]/2)

    # Combine parent and child generations
    population_start = np.concatenate((population_one, population_two))
    #print('population_start', population_start.shape)
    population_start_fitness = np.concatenate((population_one_fitness, population_two_fitness), axis=None)
    #print('population_start_fitness', population_start.shape)

    # Sorting from best to worst for total population(Decending order)
    sort_index = population_start_fitness.argsort()
    #print('sort_index', sort_index.shape)
    population_sorted = population_start[sort_index[::-1]]
    #print('population_sorted',population_sorted.shape)
    fitness_sorted = population_start_fitness[sort_index[::-1]]
    print('fitness_sorted', fitness_sorted.shape, fitness_sorted)

    # Find best induviduals and place in list
    population_top = population_sorted[:top_individuals]
    #print('population_top', population_top.shape)
    fitness_top = fitness_sorted[:top_individuals]
    #print('fitness_top', fitness_top.shape)

    # Find worst induviduals
    population_bottom = population_sorted[top_individuals:]
    #print('population_bottom', population_bottom.shape)
    # Random sample of worst individuals
    random_indices = np.random.choice(population_bottom.shape[0], random_bottom_sample)
    #print('population_bottom.shape[0]', population_bottom.shape[0])
    bottom_sample = population_bottom[random_indices]
    #print('bottom_sample', bottom_sample.shape)
    fitness_bottom = fitness_sorted[top_individuals:]
    #print('fitness_bottom', fitness_bottom.shape)
    fitness_bottom_sample = fitness_bottom[random_indices]
    #print('fitness_bottom_sample', fitness_bottom_sample.shape)

    # Combine and return
    fitness_final = np.concatenate((fitness_top, fitness_bottom_sample))
    #print('fitness_final', fitness_final.shape)
    population_final = np.concatenate((population_top, bottom_sample))
    #print('population', population_final.shape)
    return population_final, fitness_final

