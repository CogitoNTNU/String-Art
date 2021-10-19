from PIL import Image, ImageOps
import numpy as np

def get_image(path: str) -> Image:
    '''
    Returns the image at `path` in grayscale
    '''
    img = Image.open(path)
    return ImageOps.grayscale(img)

def get_fitness(image, population, n):
    '''
    Returns a list of scores from 0 to 1, based on how alike each individual in the `population` is to the original `image`
    '''
    fitness_list = np.array()

    for individual in population:
        
        # Create an image out of the individual
            # Define points where the line starts at
            # Draw the lines between the points 
        
        continue
        # Compare the images pixelwise
            # Make both image and individual image into 1d arrays and just check if they're similar
            # Similar may be, if the space is white in individual, the space in image may be up to light gray
            # and if the space is black in the individual, it can be from dark gray to black
        # Add to list of %%%s
    # Return the %%%s
    return 0