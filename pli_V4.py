import pygame, swmixer, time
from pygame.locals import *
from pygame.font import Font
from glyph import Glyph, Macros
from layer_text_placeholder import LAYERS

pygame.init()

#screen constants
pygame.display.set_caption('Poet Laureate Infinity')
#SCREEN_SIZE = (1440,852)
SCREEN_SIZE = (850, 480)
SCREEN = pygame.display.set_mode((SCREEN_SIZE), RESIZABLE)
lyrics_screen = pygame.Surface((850,140))
lyrics_screen.fill((50,50,50))
info_screen = pygame.Surface((50,50))
info_screen.fill((200,200,200))

#colors
GREEN = (0,255,0)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,255,0)
YELLOW = (0,255,255)
PURPLE = (255,255,0)
PINK = (255,0,255)
DARK_GREY = (50, 50, 50)

#image constants
BKGSCREEN = pygame.image.load("../assets/images/space_bg.jpg")
BKGSCREEN = pygame.transform.scale(BKGSCREEN, SCREEN_SIZE)
BKGSCREEN = BKGSCREEN.convert()

#font
fontObj = pygame.font.Font("../assets/fonts/garamondPro.otf", 18)
msg = 'placeholder'
GLYPH_FONT = Font("../assets/fonts/myriad.otf", 14)
FPS_FONT = pygame.font.Font("../assets/fonts/myriad.otf", 18)

#layout columns
x = SCREEN.get_width()
col2 = x*.2
col3 = x*.4
col4 = x*.6
col5 = x*.8
CLIP1 = Rect(0, 0, 160, 1000)
CLIP2 = Rect(col2, 0, 160, 1000)
CLIP3 = Rect(col3, 0, 160, 1000)
CLIP4 = Rect(col4, 0, 160, 1000)
CLIP5 = Rect(col5, 0, 160, 1000)

#swmixer
swmixer.init(samplerate=44100, chunksize=2048, stereo=True)
swmixer.start()
snd1 = swmixer.StreamingSound("../assets/audio/beatPli.mp3")
snd2 = swmixer.StreamingSound("../assets/audio/l1.mp3")
snd3 = swmixer.StreamingSound("../assets/audio/l2.mp3")
snd4 = swmixer.StreamingSound("../assets/audio/l3.mp3")
snd5 = swmixer.StreamingSound("../assets/audio/l4.mp3")
snd6 = swmixer.StreamingSound("../assets/audio/l5.mp3")

#chan1 = snd1.play()
#chan2 = snd2.play(volume=0.0)
#chan3 = snd3.play(volume=0.0)
#chan4 = snd4.play(volume=0.0)
#chan5 = snd5.play(volume=0.0)
#chan6 = snd6.play(volume=0.0)

#glyph constants
DEFAULT = {
    'bkg' : (11, 11, 11),
    'color' : (201, 192, 187),
    'font' : GLYPH_FONT,
    'spacing' : 0, #FONT.get_linesize(),
    }
glyph1 = Glyph(CLIP1, ncols=1, **DEFAULT)
glyph2 = Glyph(CLIP2, ncols=1, **DEFAULT)
glyph3 = Glyph(CLIP3, ncols=1, **DEFAULT)
glyph4 = Glyph(CLIP4, ncols=1, **DEFAULT)
glyph5 = Glyph(CLIP5, ncols=1, **DEFAULT)

Macros['green'] = ('color', GREEN)
Macros['orange'] = ('color', GREEN)

textReveal = 140
glyph1.position = [0,textReveal]
glyph2.position = [col2,textReveal]
glyph3.position = [col3,textReveal]
glyph4.position = [col4,textReveal]
glyph5.position = [col5,textReveal]

#glyph_rect1 = glyph1.rect
#glyph_rect2 = glyph2.rect
#glyph_rect3 = glyph3.rect
#glyph_rect4 = glyph4.rect
#glyph_rect5 = glyph5.rect

glyph1.input(LAYERS['1'], justify= 'left')
glyph2.input(LAYERS['2'], justify= 'left')
glyph3.input(LAYERS['3'], justify= 'left')
glyph4.input(LAYERS['4'], justify= 'left')
glyph5.input(LAYERS['5'], justify= 'left')

#glyph1.update()

#time
clock = pygame.time.Clock()
TOTAL_SECONDS = [649]
TIME = 0
accumulator = 0

#classes
class Numeral:
    beat_index = 0
    #beats = ['1', '2', '3', '4']
    
    @classmethod
    def beat(cls):
        cls.beat_index += 1
    @classmethod
    def draw(cls, screen, amount, full):
        screen_rect = screen.get_rect()
        image = FPS_FONT.render(str(cls.beat_index), True, PINK)
        rect = image.get_rect()
        #rect.center = screen_rect.center
        bpm_screen = pygame.Surface((50,50))
        bpm_screen.fill(DARK_GREY)
        bpm_screen.blit(image, rect)
        screen.blit(bpm_screen, (20, 400))

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

def scroll_lyrics():
    lyrics_screen.blit(glyph1.image, glyph1.position)
    lyrics_screen.blit(glyph2.image, glyph2.position)
    lyrics_screen.blit(glyph3.image, glyph3.position)
    lyrics_screen.blit(glyph4.image, glyph4.position)
    lyrics_screen.blit(glyph5.image, glyph5.position)

    glyph1.position[1] -= 1
    glyph2.position[1] -= 1
    glyph3.position[1] -= 1
    glyph4.position[1] -= 1
    glyph5.position[1] -= 1
   
def Tick(screen):
    global accumulator
    avg_delta = 690
    #accumulator += timeChange
    #if accumulator > timeChange:
    #    accumultor = accumulator - avg_delta
    #    Numeral.beat()
    Numeral.beat()
    Numeral.draw(screen, accumulator, avg_delta)

#__INIT__SHIT
#FPS_RENDERING = FPS_FONT.render('0', False, ORANGE)
_quit = False
pygame.time.set_timer(USEREVENT+1, 690)
pygame.time.set_timer(USEREVENT+2, 249)
chan1 = snd1.play()
chan2 = snd2.play(0.0)
chan3 = snd3.play(0.0)
chan4 = snd4.play(0.0)
chan5 = snd5.play(0.0)
chan6 = snd6.play(0.0)

while not _quit:
    clock.tick(30)
    remainingEvents = pygame.event.get()
    for e in remainingEvents:
        if (e.type is KEYDOWN and e.key == K_RETURN
                and (e.mod&(KMOD_LALT|KMOD_RALT)) != 0):
            toggle_fullscreen()
        if e.type is QUIT: _quit = True
        if e.type is KEYDOWN and e.key == K_ESCAPE: _quit = True
        if e.type == KEYDOWN and e.key == 304:
            chan2.set_volume(.5)
        if e.type == KEYUP and e.key == 304:
            chan2.set_volume(0.0)
        if e.type == KEYDOWN and e.key == 97:
            chan3.set_volume(0.5)
        if e.type == KEYUP and e.key == 97:
            chan3.set_volume(0.0)
        if e.type == KEYDOWN and e.key == 119:
            chan4.set_volume(0.5)
        if e.type == KEYUP and e.key == 119:
            chan4.set_volume(0.0)
        if e.type == KEYDOWN and e.key == 100:
            chan5.set_volume(0.5)
        if e.type == KEYUP and e.key == 100:
            chan5.set_volume(0.0)
        if e.type == KEYDOWN and e.key == 32:
            chan6.set_volume(0.5)
        if e.type == KEYUP and e.key == 32:
            chan6.set_volume(0.0)   
        if e.type == USEREVENT+1:
            Tick(SCREEN)
        if e.type == USEREVENT+2:
            scroll_lyrics()

    #scroll_lyrics()   
    
    SCREEN.blit(lyrics_screen, (0,20))
    
    pygame.display.flip()
    
pygame.quit()
