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


def state_update(stage: list):
    screen.fill((0, 0, 0))
    screen.fill(pygame.Color('White'), pygame.Rect(10, 10, 580, 580))
    screen.fill(pygame.Color('Black'), pygame.Rect(12, 12, 576, 576))
    if stage == 'menu':
        bq.h = 60
        bq.w = 120
        bq.y = 160
        b.y = 20
        b.x = 20
        #        screen.fill(pygame.Color('White'), pygame.Rect(10, 10, 580, 580))
        #        screen.fill(pygame.Color('Black'), pygame.Rect(12, 12, 576, 576))
        screen.fill(pygame.Color('Orange'), pygame.Rect(authors.x, authors.y, authors.w, authors.h))
        screen.fill(pygame.Color('Black'), pygame.Rect(authors.x + 2, authors.y + 2, authors.w - 4, authors.h - 4))
        screen.fill(pygame.Color('Orange'), pygame.Rect(b.x, b.y, b.w, b.h))
        screen.fill(pygame.Color('Black'), pygame.Rect(b.x + 2, b.y + 2, b.w - 4, b.h - 4))
        screen.fill(pygame.Color('Orange'), pygame.Rect(bq.x, bq.y, bq.w, bq.h))
        screen.fill(pygame.Color('Black'), pygame.Rect(bq.x + 2, bq.y + 2, bq.w - 4, bq.h - 4))

    elif stage == 'gameconfig':
        bq.bid = 0
        bq.y = 500
        bq.h = 60
        bq.w = 120
        screen.fill(pygame.Color('Orange'), pygame.Rect(bq.x, bq.y, bq.w, bq.h))
        screen.fill(pygame.Color('Black'), pygame.Rect(bq.x + 2, bq.y + 2, bq.w - 4, bq.h - 4))
        screen.fill(pygame.Color('Orange'), pygame.Rect(bc.x, bc.y, bc.w, bc.h))
        screen.fill(pygame.Color('Black'), pygame.Rect(bc.x + 2, bc.y + 2, bc.w - 4, bc.h - 4))
    elif stage == 'authors':
        bq.y = 500
        screen.fill(pygame.Color('Green'), pygame.Rect(250, 250, 120, 60))
    elif stage == 'game':
    elif stage == 'winnerscreen':

    b.bl = False
    authors.bl = False
    bc.bl = False
    pygame.display.update()
    return 0


def main():
    global i, state
    while window:

        clock.tick(FPS)
    pygame.time.delay(10)
    pygame.quit()








main()