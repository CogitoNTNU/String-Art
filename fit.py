import numpy as np
from skimage.metrics import structural_similarity as ssim
from draw import draw_strings

def fit(population, image, pins_xy, line_color, line_thickness):

    fitness = np.zeros((len(population)), dtype=np.double)

    string_images = draw_strings(image.shape, pins_xy, population, line_color, line_thickness)
    
    for i, img in enumerate(string_images):
        fitness[i] = ssim(image, img)

    return fitness






