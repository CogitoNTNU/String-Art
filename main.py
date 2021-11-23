from crossover import crossover
from init import initialize_population
import cv2 as cv
from fit import fit
from selection import selection
from draw import draw_strings
import numpy as np
import sys
import time
import math


np.set_printoptions(threshold=sys.maxsize)
start_time = time.time()


# NUM_INDUVIDUALS MUST BE power of two
epoch = 1
num_individual = 16
lines = 8
pins = 8
top_ratio = 2
bottom_ratio = 4
mutation_rate = 0.02
image_path = 'test-square-frame-64.png'
line_thickness = 1
line_color= (0,0,0)

image = cv.imread(image_path)
image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
w, h = image.shape
r = h/2
pins_xy = np.zeros(pins, dtype=np.dtype((np.int32, 2)))
for i in range(pins):
    rad = (i / pins) * 2 * math.pi 
    x = (w-1) / 2 + math.cos(rad) * r
    y = (h-1) / 2 + math.sin(rad) * r
    pins_xy[i] = (x,y)


first_fitness = 0
print('epcoch: 1')

init_pop = initialize_population(num_individual, lines, pins)
fitness_of_pop = fit(init_pop, image, pins_xy, line_color, line_thickness)
first_fitness = fitness_of_pop[0]

new_gen = crossover(init_pop, top_ratio, bottom_ratio, mutation_rate, pins)
fitness_new_gen = fit(new_gen, image, pins_xy, line_color, line_thickness)
best_pop, new_fitness = selection(init_pop, new_gen, fitness_of_pop, fitness_new_gen)



for i in range(epoch-1):
    new_gen = crossover(init_pop, top_ratio, bottom_ratio, mutation_rate, pins)
    fitness_new_gen = fit(new_gen, image, pins)
    best_pop, new_fitness = selection(best_pop, new_gen, new_fitness, fitness_new_gen)
   
    print('epcoch:', i+2)


string_images = draw_strings(image, pins_xy, best_pop, line_color, line_thickness)
print('first fitness', first_fitness)
print('final fitness', new_fitness[0])
print('diff:', (new_fitness[0] - first_fitness))
print('Time(min):', (time.time()- start_time)/60)
#cv.imwrite('test.png', string_images[0])
