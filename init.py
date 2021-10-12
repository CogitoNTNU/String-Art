import numpy as np
import random
#define number of lines
#define number of pins
#generate list of length lines with values 0 to pins-1
#return initialized list
#import sys
#np.set_printoptions(threshold=sys.maxsize)
'''
def initialize_single_indiuvidual(lines: int, pins: int):
    # N lines result in N+1 elements
    return np.random.randint(0, pins, size=lines+1)
'''


def initialize_population(num_induviduals: int, lines: int, pins: int):
    # Generate 2d numpy array with of containg induviduals of length lines+1
    population = np.random.randint(0, pins, size=(num_induviduals,lines+1))
    # Check if two consecutive elements are equal: if so generate new element till it is false
    for i in range(num_induviduals):
        for j in range(lines+1):
            while population[i][j] == population[i][j-1]:
                population[i][j] = random.randrange(pins)
    return population
                
#print(initialize_population(num_induviduals=3, lines=4, pins=5))

