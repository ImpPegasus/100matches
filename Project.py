import pygame

Player = 0
Opponents = 0
Count = 0
# Variables
FPS = 120
button_ch = [0, 0, [0, 4, 0, 4], int, [int, False], 0, 0]
i = 0
n = 0
g = 0
Num = button_ch[3]
Num_s = button_ch[4]
turn = int
window = False
state = ('menu', 'authors', 'gameconfig', 'game', 'winnerscreen')
vMax = 100
last = []
TC = (255, 255, 255)
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
        self.rect = pygame.Rect(x, y, w, h)
        self.line = pygame.Rect(x - 2, y - 2, w + 4, h + 4)
        self.color = pygame.Color('Black')  # (int,int,int)
        self.text = text
        self.txt = font.render(text, 1, self.color)
        self.active = False

    def Ev(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.text = ''
            else:
                self.active = False
            self.color = pygame.Color('Black') if self.active else (50, 50, 50)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = 'Player'
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text = self.text + event.unicode
                self.txt = font.render(self.text, 1, pygame.Color('White'))

    def draw(self, screen):
        screen.fill(pygame.Color('Orange'), self.line)
        screen.fill(self.color, self.rect)
        screen.blit(self.txt, (self.rect.x + 10, self.rect.y + 10))
        pygame.display.update(self.line)

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
Next = Button(11, 'Next', 505, 430, 50, 50, False, False)
Pause = Button(12, 'Pause', 450, 430, 50, 50, False, False)
Match = [
    Button(1, 'M1', 175, 215, 15, 50, True, False),  # 1 Matches
    Button(2, 'M2', 200, 215, 15, 50, True, False),  # 2 Matches
    Button(3, 'M3', 225, 215, 15, 50, True, False),  # 3 Matches
    Button(4, 'M4', 250, 215, 15, 50, True, False),  # 4 Matches
    Button(5, 'M5', 275, 215, 15, 50, True, False),  # 5 Matches
    Button(6, 'M6', 300, 215, 15, 50, True, False),  # 6 Matches
    Button(7, 'M7', 325, 215, 15, 50, True, False),  # 7 Matches
    Button(8, 'M8', 350, 215, 15, 50, True, False),  # 8 Matches
    Button(9, 'M9', 375, 215, 15, 50, True, False),  # 9 Matches
    Button(10, 'M10', 400, 215, 15, 50, True, False),  # 10 Matches
    Button(0, 'Choice', 275, 275, 50, 50, True, False)  # Choice matches
]


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
        Next.active = False
        Pause.active = False
        for MB in range(len(Match) - 1):
            Match[MB].active = False
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
        Next.active = False
        Pause.active = False
        for MB in range(len(Match) - 1):
            Match[MB].active = False
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
                # print(g_comp)
        # Game section
        Next.active = False
        Pause.active = False
        if Ut[g[1]].active == False:
            g[1] = 4
        for MB in range(len(Match) - 1):
            Match[MB].active = False
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
        if turn[0] > 0:
            Next.active = True
        else:
            Next.active = False
        Pause.active = True
        if turn[0] > 0:
            Match[10].active = True
        else:
            Match[10].active = False
        for MB in range(len(Match) - 1):
            if Num != None and Num != int:
                if Num >= 0 and not Num_s[1]:
                    Match[MB].active = True
                else:
                    Match[MB].active = False
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
    Name = ['Pause', 'Player 1', 'Player 2', 'Player 3', 'Player 4']
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
        for d in range(g[0]+1):
            Boxes[d].draw(screen)
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
        screen.fill(pygame.Color('Orange'), pygame.Rect(Match[10].x, Match[10].y, Match[10].w, Match[10].h))
        for d in range(g[0] + 1):
            Name[d + 1] = Boxes[d].text

        if Match[10].active and Num == 0 and not Num_s[1]:
            for MB in range(10):
                ChoiceButton.image = Images[0]
                ChoiceButton.rect = ChoiceButton.image.get_rect()
                Sprites.add(ChoiceButton)
                ChoiceButton.rect.x = Match[MB].x
                ChoiceButton.rect.y = Match[MB].y
                Sprites.draw(screen)
                # pygame.display.update(ChoiceButton.rect)
        elif Match[10].active and Num != None and Num != int and Num > 0 and not Num_s[1]:
            for MB in range(Num):
                ChoiceButton.image = Images[1]
                ChoiceButton.rect = ChoiceButton.image.get_rect()
                Sprites.add(ChoiceButton)
                ChoiceButton.rect.x = Match[MB].x - 5
                ChoiceButton.rect.y = Match[MB].y - 17
                Sprites.draw(screen)
            for MB in range(Num, 10):
                ChoiceButton.image = Images[0]
                ChoiceButton.rect = ChoiceButton.image.get_rect()
                Sprites.add(ChoiceButton)
                ChoiceButton.rect.x = Match[MB].x
                ChoiceButton.rect.y = Match[MB].y
                Sprites.draw(screen)
            # pygame.display.update(ChoiceButton.rect)
        else:
            screen.fill(pygame.Color('Black'),
                        pygame.Rect(Match[10].x + 2, Match[10].y + 2, Match[10].w - 4, Match[10].h - 4))
        screen.fill(pygame.Color('Orange'), pygame.Rect(bq.x, bq.y, bq.w, bq.h))
        screen.fill(pygame.Color('Black'), pygame.Rect(bq.x + 2, bq.y + 2, bq.w - 4, bq.h - 4))
        screen.fill(pygame.Color('Orange'), pygame.Rect(Next.x, Next.y, Next.w, Next.h))
        screen.fill(pygame.Color('Black'), pygame.Rect(Next.x + 2, Next.y + 2, Next.w - 4, Next.h - 4))
        screen.fill(pygame.Color('Orange'), pygame.Rect(Pause.x, Pause.y, Pause.w, Pause.h))
        screen.fill(pygame.Color('Black'), pygame.Rect(Pause.x + 2, Pause.y + 2, Pause.w - 4, Pause.h - 4))
        # screen.blit(Images[0],(Match[MB].x,Match[MB].y))
        pygame.draw.polygon(screen, pygame.Color('White'),
                            [[bq.x + 15, bq.y + 25], [bq.x + 40, bq.y + 10], [bq.x + 40, bq.y + 40]])
        if turn[0] == 0:
            pygame.draw.polygon(screen, pygame.Color('White'),
                                [[Pause.x + 40, Pause.y + 25], [Pause.x + 10, Pause.y + 10],
                                 [Pause.x + 10, Pause.y + 40]])
        else:
            screen.fill(pygame.Color('White'), pygame.Rect(Pause.x + 10, Pause.y + 10, 10, 30))
            screen.fill(pygame.Color('White'), pygame.Rect(Pause.x + 30, Pause.y + 10, 10, 30))
            screen.fill(pygame.Color('White'), pygame.Rect(Match[10].x + 10, Match[10].y + 20, 30, 6))
        button_active(3)
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
        for box in Boxes:
            box.Ev(event)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            last.append(state[i])
            # -------------------------------
            i = button_click(b) \
                or button_click(authors) \
                or button_click(bc) \
                or button_click(bq)
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
            Num = button_click(Match[0]) \
                  or button_click(Match[9]) \
                  or button_click(Match[8]) \
                  or button_click(Match[7]) \
                  or button_click(Match[6]) \
                  or button_click(Match[5]) \
                  or button_click(Match[4]) \
                  or button_click(Match[3]) \
                  or button_click(Match[2]) \
                  or button_click(Match[1]) \
                  or button_click(Match[10])
            Num_s[1] = False
            # -------------------------------
            button_ch[5] = button_click(Pause) \
                           or button_click(Next)
            # -------------------------------

            # -------------------------------

            if Num == None:
                Num = Num_s[0]
            elif Num == 0:

                if Num_s[0] != int and Num_s[0] > 0:
                    Num_s[1] = True
                    Num_s[0] = int
            else:
                Num_s[0] = Num
                Num_s[1] = False

            for g_check in range(2):
                if g[g_check] != None:
                    g[g_check + 2] = g[g_check]
                else:
                    g[g_check] = g[g_check + 2]

            if i != None:
                if n == 0 and i == 0 and state[i] == 'menu':
                    window = False
                    break
                if i == 0:
                    last = []
                elif i == 2 and n == 3:
                    for j in range(2):
                        last.pop()
                n = i
            else:
                i = n
                last.pop()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
            print(g[1])
        elif event.type == pygame.QUIT \
                or event.type == pygame.KEYDOWN \
                and event.key == pygame.K_ESCAPE \
                and last == []:
            window = False
            break
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and last != [] and turn[0] == 0:
            if len(last) < len(state):
                for d in range(len(state)):
                    if state[d] == last[len(last) - 1]:
                        i = d
                last.pop()
            else:
                print("Ошибка: Выход за пределы массива")
    return 0


def list_check(first: list):
    for f in range(len(first) - 1):
        for s in range(len(first)):
            if first[f] == first[s] and f != s:
                first.pop(s)
    return first


def main():
    global i, state, window, last
    window = True
    while window:
        state_update(state[i])
        last = list_check(last)
        Event()

        clock.tick(FPS)
    pygame.time.delay(10)
    pygame.quit()

main()