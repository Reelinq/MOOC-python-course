import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

pallo = pygame.image.load("pallo.png")

x = 0
y = 0
nopeus_x = 1
nopeus_y = 1
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(pallo, (x, y))
    pygame.display.flip()

    x += nopeus_x
    y += nopeus_y

    if x <= 0 or x + pallo.get_width() >= 640:
        nopeus_x *= -1
    if y <= 0 or y + pallo.get_height() >= 480:
        nopeus_y *= -1

    kello.tick(60)