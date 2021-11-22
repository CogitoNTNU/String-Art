import numpy as np
import math
from skimage.metrics import normalized_root_mse
import sys
import cv2 as cv

'''
np.set_printoptions(threshold=sys.maxsize)
'''
line_thickness = 1
line_color = (0,0,0)
def fit(population, image, pins):
    w, h = image.shape
    r = h/25

    pins_xy = np.zeros(pins, dtype=np.dtype((np.int32, 2)))
    fitness = np.zeros((len(population)), dtype=np.double)

    for i in range(pins):
        rad = (i / pins) * 2 * math.pi 
        x = (w-1) / 2 + math.cos(rad) * r
        y = (h-1) / 2 + math.sin(rad) * r
        pins_xy[i] = (x,y)

    for i in range(len(population)):
        string_image = np.full((w,h), 255, dtype=np.uint8)
        for j in range(1, len(population[i])): # posibly add back -1
            cv.line(string_image, pins_xy[population[i][j-1]], pins_xy[population[i][j]], color=line_color, thickness=line_thickness, lineType=cv.LINE_AA)
        fitness[i] = normalized_root_mse(image, string_image)

    return fitness



