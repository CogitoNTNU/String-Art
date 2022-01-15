import numpy as np
from skimage.metrics import structural_similarity as ssim
import sys
from draw import draw_strings
import ray

np.set_printoptions(threshold=sys.maxsize)

@ray.remote
def ssim_remote(image, string_image):
    return ssim(image, string_image)
 
def fit(population, image, pins_xy, line_color, line_thickness):

    fitness = np.zeros((len(population)), dtype=np.double)

    string_images = draw_strings(image.shape, pins_xy, population, line_color, line_thickness)
    
    obj_ref = []
    for img in string_images:
        obj_ref.append(ssim_remote.remote(image, img))

    for i, f in enumerate(obj_ref):
        fitness[i] = ray.get(f)


    return fitness






