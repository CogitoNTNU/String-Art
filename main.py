from crossover import crossover
from init import initialize_population
import cv2 as cv
from fit import fit
from selection import selection
from draw import draw
import numpy as np
import sys
import time
import math
import imageio


def main():
    np.set_printoptions(threshold=sys.maxsize)
    start_time = time.time()


    # NUM_INDUVIDUALS MUST BE power of two
    epoch = 16
    num_individual = 64
    lines = 80
    pins = 96
    top_ratio = 4
    bottom_ratio = 16
    mutation_rate = 0.125
    image_path = 'img/test-circle-frame-64.png'
    out_path_gif = 'C:/Users/jonrodtang/code/cogito/String-Art/out/outgif.gif'
    out_path_png = 'out/out.png'
    first_path_png = 'out/first.png'
    line_thickness = 1
    line_color = (0,0,0)
    gamma = 0.5
    gain = 0.5

    image = cv.imread(image_path)
    contrast_image = np.zeros(image.shape, image.dtype)
    alpha = 3
    beta = 99
    image = cv.convertScaleAbs(image, alpha=alpha, beta=beta)
    image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    cv.imwrite('out/gray.png', image)
    w, h = image.shape
    r = h/2
    pins_xy = np.zeros(pins, dtype=np.dtype((np.int32, 2)))
    for i in range(pins):
        rad = (i / pins) * 2 * math.pi 
        x = (w-1) / 2 + math.cos(rad) * r
        y = (h-1) / 2 + math.sin(rad) * r
        pins_xy[i] = (x,y)

    extra_frames = epoch//2
    images = [0] * epoch





    first_fitness = 0
    print(f'Total epochs:{epoch}')
    print('Epoch: 1')

    init_pop = initialize_population(num_individual, lines, pins)
    fitness_of_pop_init = fit(init_pop, image, pins_xy, line_color, line_thickness)
    first_fitness = fitness_of_pop_init[0]

    child_gen = crossover(init_pop, top_ratio, bottom_ratio, mutation_rate, pins)
    fitness_child_gen = fit(child_gen, image, pins_xy, line_color, line_thickness)
    best_pop, new_fitness = selection(init_pop, child_gen, fitness_of_pop_init, fitness_child_gen)

    string_image = draw(best_pop[0], line_color, line_thickness, pins_xy, image.shape)
    images[0] = string_image
    cv.imwrite(first_path_png, string_image)

    for i in range(1,epoch):
        print(f'Epoch:{i+1}')
        child_gen = crossover(best_pop, top_ratio, bottom_ratio, mutation_rate, pins)
        fitness_child_gen = fit(child_gen, image, pins_xy, line_color, line_thickness)
        best_pop, new_fitness = selection(best_pop, child_gen, new_fitness, fitness_child_gen)
    
        print(f'Percent improvment:{(new_fitness[0]-first_fitness)/first_fitness*100:.3f}%')
        images[i] = draw(best_pop[0], line_color, line_thickness, pins_xy, image.shape)




    #TODO: Convert to f strings
    print(f'First fitness{first_fitness}')
    print(f'Final fitness{new_fitness[0]}')
    print(f'Diff:{(new_fitness[0] - first_fitness):.3f}')
    print(f'Percent improvment:{(new_fitness[0]-first_fitness)/first_fitness*100:.3f}%')
    print(f'Time(min):{(time.time()- start_time)/60:.3f}')
    print(f'Time(sec) per epoch:{(time.time()- start_time)/epoch:.3f}')
    cv.imwrite(out_path_png, images[-1])
    imageio.mimsave(out_path_gif, images)


if __name__ == '__main__':
    main()
