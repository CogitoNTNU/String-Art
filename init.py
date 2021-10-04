import numpy as np
#define number of lines
#define number of pins
#generate list of length lines with values 0 to pins-1
#return initialized list
#import sys
#np.set_printoptions(threshold=sys.maxsize)

def initialization(lines: int, pins: int):
    return np.random.randint(0, pins, lines, dtype='int64')

#print(initialization(4000, 256))
