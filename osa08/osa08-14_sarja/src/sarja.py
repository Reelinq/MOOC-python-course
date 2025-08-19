class Sarja:
	def __init__(self, nimi: str, kaudet: int, genret: list):
		self.nimi = nimi
		self.kaudet = kaudet
		self.genret = genret
		self.arvostelu_summa = 0
		self.arvostelu_maara = 0
		self.keskiarvo = 0

	def arvostele(self, arvosana: int):
		self.arvostelu_summa += arvosana
		self.arvostelu_maara += 1
		self.keskiarvo = self.arvostelu_summa / self.arvostelu_maara

	def __str__(self):
		joined = ", ".join(self.genret)
		if self.arvostelu_summa == 0:
			return f"{self.nimi} ({self.kaudet} esityskautta)\ngenret: {joined}\nei arvosteluja"
		else:
			return f"{self.nimi} ({self.kaudet} esityskautta)\ngenret: {joined}\narvosteluja {self.arvostelu_maara}, keskiarvo {self.keskiarvo:.1f} pistettä"


def arvosana_vahintaan(arvosana: float, sarjat: list):
		lista = []
		for i in sarjat:
			if i.keskiarvo >= arvosana:
				lista.append(i)
		return lista

def sisaltaa_genren(genre: str, sarjat: list):
	lista = []
	for i in sarjat:
		if genre in i.genret:
			lista.append(i)
	return lista

if __name__ == "__main__":
	s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
	s1.arvostele(5)

	s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
	s2.arvostele(3)

	s3 = Sarja("Friends", 10, ["Romance", "Comendy"])
	s3.arvostele(2)

	sarjat = [s1, s2, s3]

	for sarja in arvosana_vahintaan(4.5, sarjat):
		print(sarja.nimi)

	for sarja in sisaltaa_genren("Comedy", sarjat):
		print(sarja.nimi)