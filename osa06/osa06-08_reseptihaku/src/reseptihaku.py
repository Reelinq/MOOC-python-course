def hae_tiedosto(tiedosto):
	with open (tiedosto) as recepti:
		return [i.split("\n") for i in recepti.read().rstrip().split("\n\n")]
		
def hae_nimi(tiedosto: str, sana: str):
	loytyneet = []
	for i in hae_tiedosto(tiedosto):
		if sana.lower() in i[0].lower():
			loytyneet.append(i[0])
	return loytyneet

def hae_aika(tiedosto: str, aika: int):
	loytyneet = []
	for i in hae_tiedosto(tiedosto):
		if int(i[1]) <= aika:
			loytyneet.append(i[0] + ", valmistusaika " + i[1] + " min")
	return loytyneet

def hae_raakaaine(tiedosto: str, aine: str):
	loytyneet = []
	for i in hae_tiedosto(tiedosto):
		if aine in i[2:]:
			loytyneet.append(i[0] + ", valmistusaika " + i[1] + " min")
	return loytyneet