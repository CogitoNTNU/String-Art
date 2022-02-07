import numpy as np
from skimage.metrics import structural_similarity as ssim
import sys
from draw import draw_strings
import multiprocessing


np.set_printoptions(threshold=sys.maxsize)

 
 
def fit(population, image, pins_xy, line_color, line_thickness):

    fitness = np.zeros((len(population)), dtype=np.double)
    string_images = draw_strings(image, pins_xy, population, line_color, line_thickness)
    for i in range(len(string_images)):
        fitness[i] = ssim(image, string_images[i])

    #print('fitness', fitness)
    return fitness






