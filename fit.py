import numpy as np
from skimage import io, draw
from skimage.metrics import structural_similarity as ssim 
import math
import sys

'''
image_path = 'test-square.png'
image = io.imread(image_path, as_gray=True)
pin = 15
population1 = np.random.randint(0, pin, size=(100,200+1))

np.set_printoptions(threshold=sys.maxsize)
'''

def fit(population, image, pin):
    w, h = image.shape
    r = h/2

    pins = np.empty((pin, 2), dtype=np.int32)

    fitness = np.empty((len(population)), dtype=np.double)

    for i in range(pin):
        rad = (i / pin) * 2 * math.pi 
        x = (w-1) / 2 + math.cos(rad) * r
        y = (h-1) / 2 + math.sin(rad) * r
        pins[i] = [x,y]

    for i in range(len(population)):
        string_image = np.full((w,h), 255, dtype=np.double)
        for j in range(1, len(population[i])): # posibly add back -1
            rr, cc, val = draw.line_aa(pins[population[i][j - 1]][0], pins[population[i][j - 1]][1], pins[population[i][j]][0], pins[population[i][j]][1])
            string_image[rr, cc] = val
        fitness[i] = ssim(image, string_image)

    return fitness


