# TEE RATKAISUSI TÄHÄN:
import pygame
from random import randint

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
kivi = pygame.image.load("kivi.png")

robo_x = 0
robo_y = 480 - robo.get_height()
asteroidi_x = 0
asteroidi_y = 0
pistemaara = 0

asteroidit = []

tehty = True

vasemmalle = False
oikealle = False

kello = pygame.time.Clock()

while True:
	for tapahtuma in pygame.event.get():
		if tapahtuma.type == pygame.KEYDOWN:
			if tapahtuma.key == pygame.K_LEFT:
				vasemmalle = True
			if tapahtuma.key == pygame.K_RIGHT:
				oikealle = True

		if tapahtuma.type == pygame.KEYUP:
			if tapahtuma.key == pygame.K_LEFT:
				vasemmalle = False
			if tapahtuma.key == pygame.K_RIGHT:
				oikealle = False

		if tapahtuma.type == pygame.QUIT:
			exit(0)

	naytto.fill((0, 0, 0))

	if oikealle:
		robo_x += 2
	if vasemmalle:
		robo_x -= 2

	if randint(0, 100) == 0:
		uusi_asteroidi = {
			'x': randint(0, 640 - robo.get_width()),
			'y': 0 - robo.get_height(),
			'nopeus': 1,
			'tehty': True
			}
	asteroidit.append(uusi_asteroidi)

	for asteroidi in asteroidit:
		naytto.blit(kivi, (asteroidi['x'], asteroidi['y']))
		asteroidi['y'] += asteroidi['nopeus']

		for x in range(robo_x, robo_x + robo.get_width()):
			for y in range(robo_y, robo_y + robo.get_height()):
				if asteroidi['x'] <= x <= asteroidi['x'] + kivi.get_width() and asteroidi['y'] <= y <= asteroidi['y'] + kivi.get_height():
					asteroidi['x'] = 640
					asteroidi['y'] = 480
					pistemaara += 1

	fontti = pygame.font.Font(None, 32)
	teksti = fontti.render(f"Pisteet: {pistemaara}", True, (255, 0, 0))
	naytto.blit(teksti, (640-teksti.get_width(), 0))

	naytto.blit(robo, (robo_x, robo_y))
	pygame.display.flip()

	kello.tick(60)
