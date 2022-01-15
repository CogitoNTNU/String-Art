import cv2 as cv  
import numpy as np
import concurrent.futures as cf
from itertools import repeat
from multiprocessing import cpu_count


    
def draw_strings(image_shape, pins_xy, population, line_color, line_thickness):
    (w, h) = image_shape
    population_images = np.zeros(shape=(len(population), w, h), dtype=np.uint8)

    with cf.ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        results = executor.map(draw, population, repeat(line_color), repeat(line_thickness), repeat(pins_xy), repeat(image_shape))

        for i, r in enumerate(results):
            population_images[i] = r
    return population_images


def draw(individual, line_color, line_thickness, pins_xy, image_shape):

    string_image = np.full(image_shape, 255, dtype=np.uint8)
    for j in range(1, len(individual)): # posibly add back -1
        cv.line(string_image, pins_xy[individual[j-1]], pins_xy[individual[j]], color=line_color, thickness=line_thickness, lineType=cv.LINE_AA)
    return string_image