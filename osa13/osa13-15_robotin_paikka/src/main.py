# TEE RATKAISUSI TÄHÄN:
import pygame
from random import randint

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

robo_x = 0
robo_y = 0
kohde_x = 0
kohde_y = 0

kello = pygame.time.Clock()

while True:
	for tapahtuma in pygame.event.get():
		if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
			kohde_x, kohde_y = tapahtuma.pos
			if robo_x <= kohde_x <= robo_x + robo.get_width() and robo_y <= kohde_y <= robo_y + robo.get_height():
				robo_x = randint(0, 640 - robo.get_width())
				robo_y = randint(0, 480 - robo.get_height())

		if tapahtuma.type == pygame.QUIT:
			exit(0)

	naytto.fill((0, 0, 0))
	naytto.blit(robo, (robo_x, robo_y))
	pygame.display.flip()

	kello.tick(60)
