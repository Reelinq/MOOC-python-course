from fractions import Fraction
def jaa_palasiksi(maara: int):
	palat = []
	for i in range(0, maara):
		palat.append(Fraction(1, maara))
	return palat