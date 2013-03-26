import pygame
from pygame.locals import *
from pygame.font import Font
import swmixer
from glyph import Glyph, Macros
from layer_text_placeholder import LAYERS
pygame.init()

#screen constants
pygame.display.set_caption('Poet Laureate Infinity')
#SCREEN_SIZE = (1440,852)
SCREEN_SIZE = (850, 480)
SCREEN = pygame.display.set_mode((SCREEN_SIZE), RESIZABLE)
lyrics_screen = pygame.Surface((100,100)).fill((50,50,50))

#colors
GREEN = (0,255,0)

#image constants
BKGSCREEN = pygame.image.load("../assets/images/space_bg.jpg")
BKGSCREEN = pygame.transform.scale(BKGSCREEN, SCREEN_SIZE)
BKGSCREEN = BKGSCREEN.convert()

#font
fontObj = pygame.font.Font("../assets/fonts/garamondPro.otf", 18)
msg = 'placeholder'

#functions
def center(surf, rect):
    surfrect = surf.get_rect()
    rect.x = ((surfrect.w / 2) - (rect.w / 2))
    rect.y = ((surfrect.h / 2) - (rect.h / 2))

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

#layout columns
#screen_size = pygame.display.get_surface()
x = SCREEN.get_width()
col2 = x*.2
col3 = x*.4
col4 = x*.6
col5 = x*.8
CLIP1 = Rect(0, 0, 160, 5000)
CLIP2 = Rect(col2, 0, 160, 5000)
CLIP3 = Rect(col3, 0, 160, 5000)
CLIP4 = Rect(col4, 0, 160, 5000)
CLIP5 = Rect(col5, 0, 160, 5000)

#swmixer
swmixer.init(samplerate=44100, chunksize=2048, stereo=True)
swmixer.start()
snd1 = swmixer.StreamingSound("../assets/audio/3030.mp3")
snd2 = swmixer.StreamingSound("../assets/audio/l1.mp3")
snd3 = swmixer.StreamingSound("../assets/audio/l2.mp3")
snd4 = swmixer.StreamingSound("../assets/audio/l3.mp3")
snd5 = swmixer.StreamingSound("../assets/audio/l4.mp3")
snd6 = swmixer.StreamingSound("../assets/audio/l5.mp3")

#glyph constants
FONT = Font("../assets/fonts/myriad.otf", 14)
DEFAULT = {
    'bkg' : (11, 11, 11),
    'color' : (201, 192, 187),
    'font' : FONT,
    'spacing' : 0, #FONT.get_linesize(),
    }

#time
clock = pygame.time.Clock()
TOTAL_SECONDS = [649]

class Main():

    def __init__(self):
        self.glyph1 = Glyph(CLIP1, ncols=1, **DEFAULT)
        self.glyph2 = Glyph(CLIP2, ncols=1, **DEFAULT)
        self.glyph3 = Glyph(CLIP3, ncols=1, **DEFAULT)
        self.glyph4 = Glyph(CLIP4, ncols=1, **DEFAULT)
        self.glyph5 = Glyph(CLIP5, ncols=1, **DEFAULT)
        Macros['green'] = ('color', GREEN)
        chan1 = snd1.play()
        chan2 = snd2.play(volume=0.0)
        chan3 = snd3.play(volume=0.0)
        chan4 = snd4.play(volume=0.0)
        chan5 = snd5.play(volume=0.0)
        chan6 = snd6.play(volume=0.0)

    def start(self):

        _quit = False
       
        glyph1 = self.glyph1
        glyph_rect1 = glyph1.rect
        glyph2 = self.glyph2
        glyph_rect2 = glyph2.rect
        glyph3 = self.glyph3
        glyph_rect3 = glyph3.rect
        glyph4 = self.glyph4
        glyph_rect4 = glyph4.rect
        glyph5 = self.glyph5
        glyph_rect5 = glyph5.rect
        
        glyph1.input(LAYERS['1'], justify= 'left')
        glyph2.input(LAYERS['2'], justify= 'left')
        glyph3.input(LAYERS['3'], justify= 'left')
        glyph4.input(LAYERS['4'], justify= 'left')
        glyph5.input(LAYERS['5'], justify= 'left')
        
        glyph1.update()
        glyph2.update()
        glyph3.update()
        glyph4.update()
        glyph5.update()

        #SCREEN.blit(BKGSCREEN, (0,0))
        #SCREEN.blit(glyph1.image, glyph_rect1)
        #SCREEN.blit(glyph2.image, glyph_rect2)
        #SCREEN.blit(glyph3.image, glyph_rect3)
        #SCREEN.blit(glyph4.image, glyph_rect4)
        #SCREEN.blit(glyph5.image, glyph_rect5)
        
        glyph1.position = [0,480]
        glyph2.position = [col2,480]
        glyph3.position = [col3,480]
        glyph4.position = [col4,480]
        glyph5.position = [col5,480]
        
        while not _quit:

            clock.tick(15)

            SCREEN.blit(glyph1.image, glyph1.position)
            SCREEN.blit(glyph2.image, glyph2.position)
            SCREEN.blit(glyph3.image, glyph3.position)
            SCREEN.blit(glyph4.image, glyph4.position)
            SCREEN.blit(glyph5.image, glyph5.position)
            glyph1.position[1] -= 1
            glyph2.position[1] -= 1
            glyph3.position[1] -= 1
            glyph4.position[1] -= 1
            glyph5.position[1] -= 1

            for e in pygame.event.get():
                if (e.type is KEYDOWN and e.key == K_RETURN
                        and (e.mod&(KMOD_LALT|KMOD_RALT)) != 0):
                    toggle_fullscreen()
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
            #screen = pygame.display.get_surface()
            SCREEN.blit(lyrics_screen, (50,50))
            pygame.display.flip()

if __name__ == '__main__':
    main = Main()
    main.start()
