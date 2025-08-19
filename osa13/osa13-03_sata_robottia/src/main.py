import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

naytto.fill((0, 0, 0))
korkeus = 100
for i in range(10):
	leveys = 50 + i * 10
	for i in range(10):
		naytto.blit(robo, (leveys, korkeus))
		leveys += 40
	korkeus += 20
pygame.display.flip()

while True:
	for tapahtuma in pygame.event.get():
		if tapahtuma.type == pygame.QUIT:
			exit()
