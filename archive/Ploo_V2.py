import pygame
from pygame.locals import *
from sys import exit
import swmixer

pygame.init()

swmixer.init(samplerate=44100, chunksize=2048, stereo=True)
swmixer.start()
snd1 = swmixer.StreamingSound("../assets/audio/3030.mp3")
snd2 = swmixer.StreamingSound("../assets/audio/pliLayer1.mp3")
snd3 = swmixer.StreamingSound("../assets/audio/pliLayer2.mp3")
snd4 = swmixer.StreamingSound("../assets/audio/pliLayer3.mp3")
snd5 = swmixer.StreamingSound("../assets/audio/pliLayer4.mp3")
snd6 = swmixer.StreamingSound("../assets/audio/pliLayer5.mp3")
#swmixer.set_buffersize(512)
chan1 = snd1.play()
chan2 = snd2.play(volume=0.1)
chan3 = snd3.play(volume=0.0)
chan4 = snd4.play(volume=0.0)
chan5 = snd5.play(volume=0.0)
chan6 = snd6.play(volume=0.0)
SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
while True:
    for event in pygame.event.get():
        #print event.key
        #print event.type

    #if event.type == 2 and event.key == 276:
    #   print "you did it."

        if event.type == KEYDOWN and event.key == 97:
            chan2.set_volume(0.9)
        if event.type == KEYUP:
            chan2.set_volume(0.0)
        if event.type == 2 and event.key == 97:
            chan3.set_volume(0.9)
        if event.type == 3 and event.key == 97:
            chan3.set_volume(0.0)
        if event.type == 2 and event.key == 119:
            chan4.set_volume(0.9)
        if event.type == 3 and event.key == 119:
            chan4.set_volume(0.0)
        if event.type == 2 and event.key == 100:
            chan5.set_volume(0.9)
        if event.type == 3 and event.key == 100:
            chan5.set_volume(0.0)
        if event.type == 2 and event.key == 92:
            chan6.set_volume(0.9)
        if event.type == 3 and event.key == 92:
            chan6.set_volume(0.0)

    #    if event.key == 27:
    #        exit()
        
