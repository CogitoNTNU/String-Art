import pygame as pg
import math
import numpy as np
import random
import sys

# Størrelse på bildet
w, h = (800, 800)
framerate = 60

# Pygame setup
pg.init()
screen = pg.display.set_mode((w, h))
clock = pg.time.Clock()

# Liste over spikere
pins = []

# Generer 256 spikere i en sirkel med radius 400
for i in range(256):
    rad = (i / 256.) * 2 * math.pi 
    x = w / 2 + math.cos(rad) * 400
    y = h / 2 + math.sin(rad) * 400
    pins.append((x, y))

# Tegn nye string-arts for hver iterasjon i loopen
while True:
    # Behandle input (så man kan lukke vinduet)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.event.pump()
    
    # Tegn bakgrunn
    pg.draw.rect(screen, (255, 255, 255), (0, 0, w, h))

    # Tegn spikerne som røde prikker
    for pin in pins:
        pg.draw.circle(screen, (255, 0, 0), pin, 4)

    # Generer 1000 random tråder
    population1 = np.random.randint(0, 256, size=1000+1)
    #artwork = [random.randint(0, 255) for _ in range(1000)]
    artwork = population1.tolist()


    # Tegn trådene
    for i in range(1, len(artwork) - 1):
        pg.draw.aaline(screen, (0, 0, 0), pins[artwork[i - 1]], pins[artwork[i]], 1)

    string_image = pg.image.tostring(screen, 'RGB')
    temp_surf = pg.image.fromstring(string_image,(w, h),'RGB' )
    tmp_arr = pg.surfarray.array3d(temp_surf)
    
    # Skriv til tegnebufferet
    pg.display.flip()

    # Pause for å holde frameraten stabil
    clock.tick(int(framerate))