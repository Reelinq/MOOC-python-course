# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

x = 0
x_1 = 0
y = 50
nopeus_1 = 1
nopeus_2 = 2
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y))
    naytto.blit(robo, (x_1, y+robo.get_height()))
    pygame.display.flip()

    x += nopeus_1
    x_1 += nopeus_2
    if nopeus_1 > 0 and x+robo.get_width() >= 640:
        nopeus_1 = -nopeus_1
    if nopeus_1 < 0 and x <= 0:
        nopeus_1 = -nopeus_1
    if nopeus_2 > 0 and x_1+robo.get_width() >= 640:
        nopeus_2 = -nopeus_2
    if nopeus_2 < 0 and x_1 <= 0:
        nopeus_2 = -nopeus_2

    kello.tick(60)
