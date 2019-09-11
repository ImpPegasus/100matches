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

Ut = (Button(0, font.render('1', 1, TC), 30, 70, 100, 60, True, False),
      Button(1, font.render('2', 1, TC), 135, 70, 100, 60, True, False),
      Button(2, font.render('3', 1, TC), 240, 70, 100, 60, True, False),
      Button(3, font.render('4', 1, TC), 345, 70, 100, 60, True, False),
      Button(4, font.render('0', 1, TC), 30, 180, 100, 60, True, False),
      Button(5, font.render('1', 1, TC), 135, 180, 100, 60, True, False),
      Button(6, font.render('2', 1, TC), 240, 180, 100, 60, True, False),
      Button(7, font.render('3', 1, TC), 345, 180, 100, 60, True, False))

def button_active(num: int):
    if num == 0:
        # Main section
        b.active = True
        authors.active = True
        bq.active = True
        bc.active = False
        # Ut section
        for Utc in range(0, len(Ut)):
            Ut[Utc].active = False
        # Game section

    elif num == 1:
        # Main section
        b.active = False
        authors.active = False
        bq.active = True
        bc.active = False
        # Ut section
        for Utc in range(0, len(Ut)):
            Ut[Utc].active = False
        # Game section

    elif num == 2:
        # Main section
        b.active = False
        authors.active = False
        bq.active = True
        bc.active = True
        # Ut section
        for Utc in range(0, 4):
            Ut[Utc].active = True
        if g[0] != None:
            for Utc in range(4, 8):
                Ut[Utc].active = False
            for g_comp in range(5, g[0] + 5):
                Ut[g_comp].active = True
                Ut[g_comp - 1].active = True
        # Game section

    elif num == 3:
        # Main section
        b.active = False
        authors.active = False
        bq.active = True
        bc.active = False
        # Ut section
        for Utc in range(0, len(Ut)):
            Ut[Utc].active = False
        # Game section

    return None

def button_click(but: Button):
    if event.pos[0] >= but.x \
            and event.pos[1] >= but.y \
            and event.pos[0] <= (but.x + but.w) \
            and event.pos[1] <= (but.y + but.h) \
            and but.active:
        screen.fill(pygame.Color('Orange'), pygame.Rect(but.x, but.y, but.w, but.h))
        pygame.display.update(pygame.Rect(but.x, but.y, but.w, but.h))
        pygame.time.delay(150)
        if but.bl == False:
            screen.fill(pygame.Color('Black'), pygame.Rect(but.x + 2, but.y + 2, but.w - 4, but.h - 4))
            pygame.display.update(pygame.Rect(but.x, but.y, but.w, but.h))
        return but.bid
    return None

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
        screen.fill(pygame.Color('Orange'), pygame.Rect(authors.x, authors.y, authors.w, authors.h))
        screen.fill(pygame.Color('Black'), pygame.Rect(authors.x + 2, authors.y + 2, authors.w - 4, authors.h - 4))
        screen.fill(pygame.Color('Orange'), pygame.Rect(b.x, b.y, b.w, b.h))
        screen.fill(pygame.Color('Black'), pygame.Rect(b.x + 2, b.y + 2, b.w - 4, b.h - 4))
        screen.fill(pygame.Color('Orange'), pygame.Rect(bq.x, bq.y, bq.w, bq.h))
        screen.fill(pygame.Color('Black'), pygame.Rect(bq.x + 2, bq.y + 2, bq.w - 4, bq.h - 4))

        button_active(0)
    elif stage == 'gameconfig':
        bq.bid = 0
        bq.y = 500
        bq.h = 60
        bq.w = 120
        screen.fill(pygame.Color('Orange'), pygame.Rect(bq.x, bq.y, bq.w, bq.h))
        screen.fill(pygame.Color('Black'), pygame.Rect(bq.x + 2, bq.y + 2, bq.w - 4, bq.h - 4))
        screen.fill(pygame.Color('Orange'), pygame.Rect(bc.x, bc.y, bc.w, bc.h))
        screen.fill(pygame.Color('Black'), pygame.Rect(bc.x + 2, bc.y + 2, bc.w - 4, bc.h - 4))

        for Ut_draw in range(len(Ut)):
            if Ut[Ut_draw].active:

                if Ut[Ut_draw].bid == g[1] or Ut[Ut_draw].bid == g[0]:
                    # print(Ut[Ut_draw].bid, g[0],g[1])
                    screen.fill(pygame.Color('Orange'),
                                pygame.Rect(Ut[Ut_draw].x, Ut[Ut_draw].y, Ut[Ut_draw].w, Ut[Ut_draw].h))
                else:
                    screen.fill(pygame.Color('Orange'),
                                pygame.Rect(Ut[Ut_draw].x, Ut[Ut_draw].y, Ut[Ut_draw].w, Ut[Ut_draw].h))
                    screen.fill(pygame.Color('Black'),
                                pygame.Rect(Ut[Ut_draw].x + 2, Ut[Ut_draw].y + 2, Ut[Ut_draw].w - 4, Ut[Ut_draw].h - 4))
            else:
                screen.fill(pygame.Color('Gray'),
                            pygame.Rect(Ut[Ut_draw].x, Ut[Ut_draw].y, Ut[Ut_draw].w, Ut[Ut_draw].h))

        for Ut_tex in range(8):
            # if Ut[Ut_tex].active:
            screen.blit(Ut[Ut_tex].tex, (Ut[Ut_tex].x + 45, Ut[Ut_tex].y + 20))
        button_active(2)
    elif stage == 'authors':
        bq.y = 500
        screen.fill(pygame.Color('Orange'), pygame.Rect(bq.x, bq.y, bq.w, bq.h))
        screen.fill(pygame.Color('Black'), pygame.Rect(bq.x + 2, bq.y + 2, bq.w - 4, bq.h - 4))
        screen.blit(font.render("Made by Drobot", 1, TC), (250, 250))
        screen.blit(bq.tex, (bq.x + 40, bq.y + 20))
        button_active(1)
    elif stage == 'game':
        bq.bid = 2
        bq.w = 60
        bq.h = 50
        bq.y = 530
        screen.fill(pygame.Color('Orange'), pygame.Rect(bq.x, bq.y, bq.w, bq.h))
        screen.fill(pygame.Color('Black'), pygame.Rect(bq.x + 2, bq.y + 2, bq.w - 4, bq.h - 4))
        screen.fill(pygame.Color('Orange'), pygame.Rect(Next.x, Next.y, Next.w, Next.h))
        screen.fill(pygame.Color('Black'), pygame.Rect(Next.x + 2, Next.y + 2, Next.w - 4, Next.h - 4))
        screen.fill(pygame.Color('Orange'), pygame.Rect(Pause.x, Pause.y, Pause.w, Pause.h))
        screen.fill(pygame.Color('Black'), pygame.Rect(Pause.x + 2, Pause.y + 2, Pause.w - 4, Pause.h - 4))
    elif stage == 'winnerscreen':
        screen.fill(pygame.Color('Orange'), pygame.Rect(bq.x, bq.y, bq.w, bq.h))
        screen.fill(pygame.Color('Black'), pygame.Rect(bq.x + 2, bq.y + 2, bq.w - 4, bq.h - 4))

    b.bl = False
    authors.bl = False
    bc.bl = False
    pygame.display.update()
    return 0

def Event():
    global i, n, g, last, event, turn, window, Num, Num_s, Player, Opponents, bool, Count
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            last.append(state[i])
            i = button_click(b) or button_click(authors) or button_click(bc) or button_click(bq) or button_click(Ut1) or button_click(Ut2) or button_click(Ut3) or button_click(Ut4) or button_click(Ut5) or button_click(Ut6) or button_click(Ut7) or button_click(Ut8)
            # -------------------------------
            g[0] = button_click(Ut[3]) \
                   or button_click(Ut[2]) \
                   or button_click(Ut[1]) \
                   or button_click(Ut[0])
            # -------------------------------
            g[1] = button_click(Ut[7]) \
                   or button_click(Ut[6]) \
                   or button_click(Ut[5]) \
                   or button_click(Ut[4])
            # -------------------------------
            for g_check in range(2):
                if g[g_check] != None:
                    g[g_check + 2] = g[g_check]
                else:
                    g[g_check] = g[g_check + 2]
        elif event.type == pygame.QUIT \
                or event.type == pygame.KEYDOWN \
                and event.key == pygame.K_ESCAPE \
                and last == [] or bq.bl and state[i] == 'menu':
            window = False
            break
        return 0

def main():
    global i, state, window
    window = True
    while window:
        state_update(state[i])
        Event()

        clock.tick(FPS)
    pygame.time.delay(10)
    pygame.quit()








main()