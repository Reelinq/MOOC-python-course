def tallenna_henkilo(henkilo: tuple):
	with open ("henkilot.csv", "a") as tiedosto:
		tiedosto.write(henkilo[0] + ";" + str(henkilo[1]) + ";" + str(henkilo[2]))