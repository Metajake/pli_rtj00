import pygame
from pygame.locals import *

pygame.init()

song = pygame.mixer.Sound('../assets/audio/beatPli.ogg')
clock = pygame.time.Clock()
song.play()
screen = pygame.display.set_mode((399, 299))
while True:
    clock.tick(240)
    for event in pygame.event.get():
        if event.type == KEYDOWN: 
            if event.key == 97:
                song.set_volume(0.0)
        if event.type == KEYUP:        
            if event.key == 97:
                song.set_volume(1.0)        
pygame.quit()
