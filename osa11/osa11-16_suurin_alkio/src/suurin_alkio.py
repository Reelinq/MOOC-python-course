# TEE RATKAISUSI TÄHÄN:
class Alkio:
	""" Luokka mallintaa yhtä alkiota binääripuussa """
	def __init__(self, arvo, vasen_lapsi:'Alkio' = None, oikea_lapsi:'Alkio' = None):
		self.arvo = arvo
		self.vasen_lapsi = vasen_lapsi
		self.oikea_lapsi = oikea_lapsi


def suurin_alkio(juuri: Alkio):
	suurin = juuri.arvo
	if juuri.vasen_lapsi is not None:
		if suurin_alkio(juuri.vasen_lapsi) > suurin:
			suurin = suurin_alkio(juuri.vasen_lapsi)

	if juuri.oikea_lapsi is not None:
		if suurin_alkio(juuri.oikea_lapsi) > suurin:
			suurin = suurin_alkio(juuri.oikea_lapsi)

	return suurin
