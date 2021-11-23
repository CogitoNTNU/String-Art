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
epoch = 128
num_individual = 256
lines = 1000
pins = 256
top_ratio = 2
bottom_ratio = 8
mutation_rate = 0.125
image_path = 'space-woman.jpg'
line_thickness = 1
line_color= (0,0,0)

image = cv.imread(image_path)
image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
cv.imwrite('gray.png', image)
w, h = image.shape
r = h/2
pins_xy = np.zeros(pins, dtype=np.dtype((np.int32, 2)))
for i in range(pins):
    rad = (i / pins) * 2 * math.pi 
    x = (w-1) / 2 + math.cos(rad) * r
    y = (h-1) / 2 + math.sin(rad) * r
    pins_xy[i] = (x,y)


first_fitness = 0
print('Total epochs:', epoch)
print('Epoch: 1')

init_pop = initialize_population(num_individual, lines, pins)
fitness_of_pop_init = fit(init_pop, image, pins_xy, line_color, line_thickness)
first_fitness = fitness_of_pop_init[0]

child_gen = crossover(init_pop, top_ratio, bottom_ratio, mutation_rate, pins)
fitness_child_gen = fit(child_gen, image, pins_xy, line_color, line_thickness)
best_pop, new_fitness = selection(init_pop, child_gen, fitness_of_pop_init, fitness_child_gen)


string_images = draw_strings(image, pins_xy, best_pop, line_color, line_thickness)
cv.imwrite('test.png', string_images[0])

for i in range(epoch-1):
    child_gen = crossover(best_pop, top_ratio, bottom_ratio, mutation_rate, pins)
    fitness_child_gen = fit(child_gen, image, pins_xy, line_color, line_thickness)
    best_pop, new_fitness = selection(best_pop, child_gen, new_fitness, fitness_child_gen)
   
    print('Epoch:', i+2)
    if (i+2)%16 == 0:
        print('Percent improvment:{:.3f}%'.format((new_fitness[0]-first_fitness)/first_fitness*100))
        string_images = draw_strings(image, pins_xy, best_pop, line_color, line_thickness)
        cv.imwrite('test.png', string_images[0])





print('First fitness', first_fitness)
print('Final fitness', new_fitness[0])
print('Diff:{:.3f}'.format((new_fitness[0] - first_fitness)))
print('Percent improvment:{:.3f}%'.format((new_fitness[0]-first_fitness)/first_fitness*100))
print('Time(min):{:.3f}'.format((time.time()- start_time)/60))
print('Time(sec) per epoch:{:.3f}'.format((time.time()- start_time)/epoch))
string_images = draw_strings(image, pins_xy, best_pop, line_color, line_thickness)
cv.imwrite('test.png', string_images[0])
