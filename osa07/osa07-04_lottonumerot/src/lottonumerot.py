from random import sample
def lottonumerot(maara: int, alaraja: int, ylaraja: int):
	kaikki_luvut = list(range(alaraja, ylaraja))
	rivi = sample(kaikki_luvut, maara)
	rivi.sort()
	return rivi