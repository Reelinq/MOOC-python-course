# TEE RATKAISUSI TÄHÄN:
import pygame
from random import randint

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

naytto.fill((0, 0, 0))
for i in range(1000):
	leveys = randint(0, 640-robo.get_width())
	korkeus = randint(0, 480-robo.get_height())
	naytto.blit(robo, (leveys, korkeus))
pygame.display.flip()

while True:
	for tapahtuma in pygame.event.get():
		if tapahtuma.type == pygame.QUIT:
			exit()
