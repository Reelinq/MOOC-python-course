def lisaa_elokuva(rekisteri: list, nimi: str, ohjaaja: str, vuosi: int, pituus: int):
	elokuva = {
		"nimi": nimi,
		"ohjaaja": ohjaaja,
		"vuosi": vuosi,
		"pituus": pituus
	}
	rekisteri.append(elokuva)


if __name__ == "__main__":
	rekisteri = []
	lisaa_elokuva(rekisteri, "Pythonin viemää", "Pekka Python", 2017, 116)
	lisaa_elokuva(rekisteri, "Python lentokoneessa", "Renny Pytholin", 2001, 94)
	print(rekisteri)
