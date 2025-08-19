# TEE RATKAISUSI TÄHÄN:
import pygame
from datetime import datetime
import math

pygame.init()
naytto = pygame.display.set_mode((640, 480))
kello = pygame.time.Clock()

while True:
	naytto.fill((0, 0, 0))
	pygame.draw.circle(naytto, (255, 0, 0), (320, 240), 200)
	pygame.draw.circle(naytto, (0, 0, 0), (320, 240), 195)
	pygame.draw.circle(naytto, (255, 0, 0), (320, 240), 10)

	aika = datetime.now()
	pygame.display.set_caption(aika.strftime("%H:%M:%S"))

	tunnit = aika.hour % 12
	minuutit = aika.minute
	sekunnit = aika.second

	pygame.draw.line(naytto, (0, 0, 255), (320, 240), (320 + math.cos(tunnit * (2 * math.pi / 12) -
					 math.pi/2) * 175, 240 + math.sin(tunnit * (2 * math.pi / 12) - math.pi/2) * 175), 5)
	pygame.draw.line(naytto, (0, 0, 255), (320, 240), (320 + math.cos(minuutit * (2 * math.pi / 60) -
					 math.pi/2) * 175, 240 + math.sin(minuutit * (2 * math.pi / 60) - math.pi/2) * 175), 2)
	pygame.draw.line(naytto, (0, 0, 255), (320, 240), (320 + math.cos(sekunnit * (2 * math.pi / 60) -
					 math.pi/2) * 175, 240 + math.sin(sekunnit * (2 * math.pi / 60) - math.pi/2) * 175), 1)

	pygame.display.flip()

	for tapahtuma in pygame.event.get():
		if tapahtuma.type == pygame.QUIT:
			exit()

	kello.tick(60)
