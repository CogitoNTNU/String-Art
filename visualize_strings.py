import pygame as pg
import math
import numpy as np
import random

# Størrelse på bildet
w, h = (1000, 1000)
framerate = 10

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
    artwork = [random.randint(0, 255) for _ in range(1000)]

    # Tegn trådene
    for i in range(1, len(artwork) - 1):
        pg.draw.aaline(screen, (0, 0, 0), pins[artwork[i - 1]], pins[artwork[i]], 1)
    
    # Skriv til tegnebufferet
    pg.display.flip()

    # Pause for å holde frameraten stabil
    clock.tick(int(framerate))