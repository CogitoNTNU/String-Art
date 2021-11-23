import cv2 as cv  
import math
import numpy as np
    



    
def draw(image, pins, population, line_color, line_thickness):
    pins_xy = np.zeros(pins, dtype=np.dtype((np.int32, 2)))
    w, h = image.shape
    r = h/25
    for i in range(pins):
        rad = (i / pins) * 2 * math.pi 
        x = (w-1) / 2 + math.cos(rad) * r
        y = (h-1) / 2 + math.sin(rad) * r
        pins_xy[i] = (x,y)

    population_images = np.zeros(population.shape)
    for i in range(len(population)):
        string_image = np.full((w,h), 255, dtype=np.uint8)
        for j in range(1, len(population[i])): # posibly add back -1
            cv.line(string_image, pins_xy[population[i][j-1]], pins_xy[population[i][j]], color=line_color, thickness=line_thickness, lineType=cv.LINE_AA)
        population_images[i] = string_image
    
    return population_images
        