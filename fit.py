import numpy as np
import math
from skimage.metrics import structural_similarity as ssim
import sys
import cv2 as cv


np.set_printoptions(threshold=sys.maxsize)

 
 
def fit(population, image, pins, line_color=(0,0,0), line_thickness=1):

    fitness = np.zeros((len(population)), dtype=np.double)

    string_images = draw(image, pins, population, line_color, line_thickness)
    for i in range(len(string_images)):
        fitness[i] = ssim(image, string_images[i])

    print(fitness)
    return fitness





