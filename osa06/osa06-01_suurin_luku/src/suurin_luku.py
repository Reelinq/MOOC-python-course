def suurin():
	with open("luvut.txt") as tiedosto:
		suurin = 0
		for i in tiedosto:
			if suurin < int(i):
				suurin = int(i)
	return suurin