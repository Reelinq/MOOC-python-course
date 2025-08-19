x = 0
y = 0
nopeus_x = 1
nopeus_y = 0
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y))
    pygame.display.flip()

    x += nopeus_x
    y += nopeus_y
    if nopeus_x > 0 and x+robo.get_width() >= 640:
        nopeus_x = 0
        nopeus_y = 1
    if nopeus_x < 0 and x <= 0:
        nopeus_x = 0
        nopeus_y = -1
    if nopeus_y > 0 and y+robo.get_height() >= 480:
        nopeus_y = 0
        nopeus_x = -1
    if nopeus_y < 0 and y <= 0:
        nopeus_y = 0
        nopeus_x = 1