import random
#define number of lines
#define number of pins
#generate list of length lines with values 0 to pins-1
#return initialized list

def initialization(lines: int, pins: int):
    initList = []
    for i in range(lines):
        initList.append(random.randint(0, pins))

    return initList

#print(initialization(4000, 256))
