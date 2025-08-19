import math

def hae_asematiedot(tiedosto: str):
	asematiedot = {}
	with open (tiedosto) as kaupunkipyorat:
		for i in kaupunkipyorat:
			j = i.replace("\n", "").split(";")
			if j[0] == "Longitude":
				continue
			else:
				asematiedot[j[3]] = (float(j[0]), float(j[1]))
	return asematiedot

def etaisyys(asemat: dict, asema1: str, asema2: str):
	uusi_asema1 = asemat.get(asema1)
	uusi_asema2 = asemat.get(asema2)
	x_kilometreina = (uusi_asema1[0] - uusi_asema2[0]) * 55.26
	y_kilometreina = (uusi_asema1[1] - uusi_asema2[1]) * 111.2
	etaisyys = math.sqrt(x_kilometreina**2 + y_kilometreina**2)
	return etaisyys

def suurin_etaisyys(asemat: dict):
	at_items = list(asemat.items())
	suurin = ("", "", 0)
	for i in range(len(at_items)-1):
		nimi1, sijainti1 = at_items[i]
		for j in range(i+1, len(at_items)):
			nimi2, sijainti2 = at_items[j]

			x_kilometreina = (sijainti1[0] - sijainti2[0]) * 55.26
			y_kilometreina = (sijainti1[1] - sijainti2[1]) * 111.2
			etaisyys = math.sqrt(x_kilometreina**2 + y_kilometreina**2)

			if etaisyys > suurin[2]:
				suurin = (nimi1, nimi2, etaisyys)
	return suurin