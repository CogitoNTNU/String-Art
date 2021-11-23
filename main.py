from crossover import crossover
from init import initialize_population
import cv2 as cv
from fit import fit
from selection import selection
import numpy as np
import math
import sys
import time


np.set_printoptions(threshold=sys.maxsize)
start_time = time.time()


# NUM_INDUVIDUALS MUST BE power of two
epoch = 1
num_individual = 4
lines = 8
pins = 4
top_ratio = 2
bottom_ratio = 2
mutation_rate = 0.02
image_path = 'test-square-frame-64.png'
line_thickness = 1
line_color= (0,0,0)

image = cv.imread(image_path)
image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
w,h = image.shape
r = h/2
first_fitness = 0


init_pop = initialize_population(num_individual, lines, pins)
fitness_of_pop = fit(init_pop, image, pins)
new_gen = crossover(init_pop, top_ratio, bottom_ratio, mutation_rate, pins)
fitness_new_gen = fit(new_gen, image, pins)
best_pop, new_fitness = selection(init_pop, new_gen, fitness_of_pop, fitness_new_gen)
print('epcoch: 1')
for i in range(1):
    pins_xy = np.zeros(pins, dtype=np.dtype((np.int32, 2))) 
    print('Top fitness', new_fitness[0])
    first_fitness = new_fitness[0]
    for i in range(pins):
        rad = (i / pins) * 2 * math.pi 
        x = (w-1) / 2 + math.cos(rad) * r
        y = (h-1) / 2 + math.sin(rad) * r
        pins_xy[i] = (x,y)

    string_image = np.full((w, h), 255, dtype=np.double)
    for j in range(1, len(best_pop[0])): # posibly add back -1
        cv.line(string_image, pins_xy[best_pop[0][j-1]], pins_xy[best_pop[0][j]], color=line_color, thickness=line_thickness, lineType=cv.LINE_AA)
    cv.imwrite('test.png', string_image)
for i in range(epoch-1):
    new_gen = crossover(init_pop, top_ratio, bottom_ratio, mutation_rate, pins)
    fitness_new_gen = fit(new_gen, image, pins)
    best_pop, new_fitness = selection(best_pop, new_gen, new_fitness, fitness_new_gen)
   
    print('epcoch:', i+2)
'''
    if (((i+2)%2) == 0):
        pins_xy = np.zeros(pins, dtype=np.dtype((np.int32, 2)))
        print('Top fitness', new_fitness[0])
        for i in range(pins):
            rad = (i / pins) * 2 * math.pi 
            x = (w-1) / 2 + math.cos(rad) * r
            y = (h-1) / 2 + math.sin(rad) * r
            pins_xy[i] = (x,y)

        string_image = np.full((w, h), 255, dtype=np.double)
        for j in range(1, len(best_pop[0])): # posibly add back -1
            cv.line(string_image, pins_xy[best_pop[0][j-1]], pins_xy[best_pop[0][j]], color=line_color, thickness=line_thickness, lineType=cv.LINE_AA)
        cv.imwrite('test.png', string_image)
'''


string_images = draw(image, pins, population, line_color, line_thickness)
print(new_fitness[0])
print('diff:', (new_fitness[0] - first_fitness)*100)
print('Time(min):', (time.time()- start_time)/60)
cv.imwrite('test.png', string_images[0])