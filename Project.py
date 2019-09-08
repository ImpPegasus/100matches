import pygame

# Variables
FPS = 120
button_ch = [0, 0, [0, 4, 0, 4], int, [int, False], 0, 0]
i = 0
n = 0
g = 0
turn = int
window = False
state = ('menu', 'authors', 'gameconfig', 'game', 'winnerscreen')
vMax = 100
last = str
size = width, height = (600, 600)

# Init functions
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Thin Skinned', 25)
Images = [pygame.image.load('m1_1.png').convert_alpha(),
          pygame.image.load('m1f_1.png').convert_alpha(),
          pygame.image.load('m1f90.png').convert_alpha(),
          pygame.image.load('m190.png').convert_alpha()]
Sprites = pygame.sprite.Group()
ChoiceButton = pygame.sprite.Sprite()

class Input_Box(object):
    def __init__(self, x, y, w, h, text=''):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.line = pygame.Rect(x - 2, y - 2, w + 4, h + 4)
        self.color = pygame.Color('Black')  # (int,int,int)
        self.text = text
        self.txt = font.render(text, 1, self.color)
        self.active = False


Boxes = [Input_Box(120, 300, 140, 32, 'Player 1'),
         Input_Box(120, 340, 140, 32, 'Player 2'),
         Input_Box(120, 380, 140, 32, 'Player 3'),
         Input_Box(120, 420, 140, 32, 'Player 4')]

class Button(object):
    def __init__(self, bid, tex, x, y, w, h, bl, active):
        self.bid = bid
        self.tex = tex
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.bl = bl
        self.active = active

b = Button(2, font.render('Start', 1, TC), 20, 20, 120, 60, False, False)
bc = Button(3, font.render('Start', 1, TC), 450, 500, 120, 60, False, False)
bq = Button(0, font.render('Quit', 1, TC), 20, 160, 120, 60, False, False)
authors = Button(1, font.render('Authors', 1, TC), 20, 90, 120, 60, False, False)





def main():
    global i, state
    while window:

        clock.tick(FPS)
    pygame.time.delay(10)
    pygame.quit()








main()