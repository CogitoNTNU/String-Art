import cv2 as cv  
import numpy as np
import ray


@ray.remote
def draw(individual, line_color, line_thickness, pins_xy, image_shape):

    string_image = np.full(image_shape, 255, dtype=np.uint8)
    for j in range(1, len(individual)): # posibly add back -1
        cv.line(string_image, pins_xy[individual[j-1]], pins_xy[individual[j]], color=line_color, thickness=line_thickness, lineType=cv.LINE_AA)
    return string_image


def draw_strings(image_shape, pins_xy, population, line_color, line_thickness):
    (w, h) = image_shape
    population_images = np.zeros(shape=(len(population), w, h), dtype=np.uint8)
    obj_ref = []
    for individual in population:
        obj_ref.append(draw.remote(individual, line_color, line_thickness, pins_xy, image_shape))

    for i, img in enumerate(obj_ref):
        population_images[i] = ray.get(img)

    return population_images



