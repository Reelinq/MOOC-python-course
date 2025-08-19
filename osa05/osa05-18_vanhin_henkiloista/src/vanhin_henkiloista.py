def vanhin(henkilot: list):

	vanhin_henkilo = henkilot[0]
	for i in henkilot:
		if i[1] < vanhin_henkilo[1]:
			vanhin_henkilo = i
	return vanhin_henkilo[0]

if __name__ == "__main__":
	h1 = ("Arto", 1977)
	h2 = ("Einari", 1985)
	h3 = ("Maija", 1953)
	h4 = ("Essi", 1997)
	hlista = [h1, h2, h3, h4]

	print(vanhin(hlista))