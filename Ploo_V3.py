import pygame
from pygame.locals import *
import swmixer 
 
swmixer.init(samplerate=44100, chunksize=2048, stereo=True)
swmixer.start()
snd1 = swmixer.StreamingSound("../assets/audio/3030.mp3")
snd2 = swmixer.StreamingSound("../assets/audio/l1.mp3")
snd3 = swmixer.StreamingSound("../assets/audio/l2.mp3")
snd4 = swmixer.StreamingSound("../assets/audio/l3.mp3")
snd5 = swmixer.StreamingSound("../assets/audio/l4.mp3")
snd6 = swmixer.StreamingSound("../assets/audio/l5.mp3")

chan1 = snd1.play()
chan2 = snd2.play(volume=0.0)
chan3 = snd3.play(volume=0.0)
chan4 = snd4.play(volume=0.0)
chan5 = snd5.play(volume=0.0)
chan6 = snd6.play(volume=0.0)

def toggle_fullscreen():
    screen = pygame.display.get_surface()
    tmp = screen.convert()
    caption = pygame.display.get_caption()
    cursor = pygame.mouse.get_cursor()  # Duoas 16-04-2007 
    
    w,h = screen.get_width(),screen.get_height()
    flags = screen.get_flags()
    bits = screen.get_bitsize()
    
    pygame.display.quit()
    pygame.display.init()
    
    screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)
    screen.blit(tmp,(0,0))
    pygame.display.set_caption(*caption)
 
    pygame.key.set_mods(0) #HACK: work-a-round for a SDL bug??
 
    pygame.mouse.set_cursor( *cursor )  # Duoas 16-04-2007
    
    return screen
 
if __name__ == '__main__':
    SW,SH = 640,480
    screen = pygame.display.set_mode((SW,SH), FULLSCREEN)
    pygame.display.set_caption('this is a test')
    
    _quit = False
    while not _quit:
        for e in pygame.event.get():
            #if (e.type is KEYDOWN and e.key == K_RETURN
            #        and (e.mod&(KMOD_LALT|KMOD_RALT)) != 0):
            #    toggle_fullscreen()
            if e.type is QUIT: _quit = True
            if e.type is KEYDOWN and e.key == K_ESCAPE: _quit = True
            if e.type == KEYDOWN and e.key == 304:
                chan2.set_volume(1.0)
            if e.type == KEYUP and e.key == 304:
                chan2.set_volume(0.0)
            if e.type == KEYDOWN and e.key == 97:
                chan3.set_volume(1.0)
            if e.type == KEYUP and e.key == 97:
                chan3.set_volume(0.0)
            if e.type == KEYDOWN and e.key == 119:
                chan4.set_volume(1.0)
            if e.type == KEYUP and e.key == 119:
                chan4.set_volume(0.0)
            if e.type == KEYDOWN and e.key == 100:
                chan5.set_volume(1.0)
            if e.type == KEYUP and e.key == 100:
                chan5.set_volume(0.0)
            if e.type == KEYDOWN and e.key == 32:
                chan6.set_volume(1.0)
            if e.type == KEYUP and e.key == 32:
                chan6.set_volume(0.0)   
        screen = pygame.display.get_surface()
        pygame.display.flip()




