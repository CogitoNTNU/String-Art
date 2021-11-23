import cv2 as cv  
import numpy as np
    



    
def draw_strings(image, pins_xy, population, line_color, line_thickness):
    w, h = image.shape

    population_images = np.zeros(shape=(len(population), w, h), dtype=np.uint8)
    for i in range(len(population)):
        string_image = np.full(image.shape, 255, dtype=np.uint8)
        for j in range(1, len(population[i])): # posibly add back -1
            cv.line(string_image, pins_xy[population[i][j-1]], pins_xy[population[i][j]], color=line_color, thickness=line_thickness, lineType=cv.LINE_AA)
        population_images[i] = string_image
        #cv.imwrite('test.png', string_image)
    
    return population_images
        