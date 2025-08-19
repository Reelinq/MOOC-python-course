# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

kello = pygame.time.Clock()

robotit = [{"x": 0, "y": 480-robo.get_height(), "vasemmalle": False, "oikealle": False, "ylos": False, "alas": False, "vasen_ohjaus": pygame.K_LEFT, "oikea_ohjaus": pygame.K_RIGHT, "ylos_ohjaus": pygame.K_UP, "alas_ohjaus": pygame.K_DOWN},
			{"x": 640-robo.get_width(), "y": 480-robo.get_height(), "vasemmalle": False, "oikealle": False, "ylos": False, "alas": False, "vasen_ohjaus": pygame.K_a, "oikea_ohjaus": pygame.K_d, "ylos_ohjaus": pygame.K_w, "alas_ohjaus": pygame.K_s}]

while True:
	naytto.fill((0, 0, 0))
	tapahtumat = pygame.event.get()
	for robot in robotit:
		for tapahtuma in tapahtumat:
			if tapahtuma.type == pygame.KEYDOWN:
				if tapahtuma.key == robot["vasen_ohjaus"]:
					robot["vasemmalle"] = True
				if tapahtuma.key == robot["oikea_ohjaus"]:
					robot["oikealle"] = True
				if tapahtuma.key == robot["ylos_ohjaus"]:
					robot["ylos"] = True
				if tapahtuma.key == robot["alas_ohjaus"]:
					robot["alas"] = True

			if tapahtuma.type == pygame.KEYUP:
				if tapahtuma.key == robot["vasen_ohjaus"]:
					robot["vasemmalle"] = False
				if tapahtuma.key == robot["oikea_ohjaus"]:
					robot["oikealle"] = False
				if tapahtuma.key == robot["ylos_ohjaus"]:
					robot["ylos"] = False
				if tapahtuma.key == robot["alas_ohjaus"]:
					robot["alas"] = False

			if tapahtuma.type == pygame.QUIT:
				exit()

		if robot["vasemmalle"] and robot["x"] > 0:
			robot["x"] -= 2
		if robot["oikealle"] and robot["x"] + robo.get_width() < 640:
			robot["x"] += 2
		if robot["ylos"] and robot["y"] > 0:
			robot["y"] -= 2
		if robot["alas"] and robot["y"] + robo.get_height() < 480:
			robot["y"] += 2

		naytto.blit(robo, (robot["x"], robot["y"]))

	pygame.display.flip()
	kello.tick(60)
