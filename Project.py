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
