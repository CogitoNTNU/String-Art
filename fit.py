import numpy as np
from skimage.metrics import structural_similarity as ssim
import sys
from draw import draw_strings
import concurrent.futures as cf
from itertools import repeat
from multiprocessing import cpu_count

np.set_printoptions(threshold=sys.maxsize)

 
 
def fit(population, image, pins_xy, line_color, line_thickness):

    fitness = np.zeros((len(population)), dtype=np.double)

    string_images = draw_strings(image.shape, pins_xy, population, line_color, line_thickness)

    with cf.ThreadPoolExecutor(max_workers=cpu_count()) as executor:
        results = executor.map(ssim, repeat(image), string_images)

        for i, r in enumerate(results):
            fitness[i] = r


    return fitness






