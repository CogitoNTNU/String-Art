import numpy as np

pins = 256
num_induviduals = 4
lines = 12
population1 = np.random.randint(0, pins, size=(num_induviduals,lines+1))
population2 = np.random.randint(0, pins, size=(num_induviduals,lines+1))
population1_fit = np.random.rand(1,num_induviduals)
population2_fit = np.random.rand(1,num_induviduals)

def selection(population_one, population_two, population_one_fitness, population_two_fitness,):

    top_individuals = int(population_one.shape[0]/2)
    random_bottom_sample = int(population_one.shape[0]/2)

    population_start = np.concatenate((population_one, population_two))
    population_start_fitness = np.concatenate((population_one_fitness, population_two_fitness), axis=None)


    # Sorting from best to worst for total population(Decending order)
    sort_index = population_start_fitness.argsort()
    population_sorted = population_start[sort_index[::-1]]
    fitness_sorted = population_start_fitness[sort_index[::-1]]

    # Find best induviduals and place in list
    population_top = population_sorted[:top_individuals]
    fitness_top = fitness_sorted[:top_individuals]

    # Find worst induviduals
    population_bottom = population_sorted[top_individuals:]
    # Random sample of worst individuals
    random_indices = np.random.choice(population_bottom.shape[0], random_bottom_sample)
    bottom_sample = population_bottom[random_indices]
    fitness_bottom = fitness_sorted[top_individuals:]
    fitness_bottom_sample = fitness_bottom[random_indices]

    # Combine and return
    fitness_final = np.concatenate((fitness_top, fitness_bottom_sample))
    population_final = np.concatenate((population_top, bottom_sample))
    return population_final, fitness_final


print(selection(population1, population2, population1_fit, population2_fit))