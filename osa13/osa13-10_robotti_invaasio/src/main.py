# TEE RATKAISUSI TÄHÄN:
import pygame
from random import randint

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
robots = []
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))

    if randint(0, 50) == 0:
        new_robot = {
            'x': randint(0, 640 - robo.get_width()),
            'y': 0 - robo.get_height(),
            'nopeus_x': 0,
            'nopeus_y': 1,
            'tehty': True
        }
        robots.append(new_robot)

    for robot in robots:
        naytto.blit(robo, (robot['x'], robot['y']))
        robot['x'] += robot['nopeus_x']
        robot['y'] += robot['nopeus_y']

        if robot['y'] + robo.get_height() == 480 and robot['tehty']:
            robot['tehty'] = False
            robot['nopeus_y'] = 0
            robot['nopeus_x'] = 1 if randint(0, 1) == 0 else -1

    pygame.display.flip()
    kello.tick(60)
