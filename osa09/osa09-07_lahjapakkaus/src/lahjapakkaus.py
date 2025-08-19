class Lahja:
	def __init__(self, nimi: str, paino: int):
		self.nimi = nimi
		self.paino = paino

	def __str__(self):
		return f"{self.nimi} ({self.paino} kg)"


class Pakkaus:
	def __init__(self):
		self.lahjojen_yhteispaino = 0

	def lisaa_lahja(self, lahja: Lahja):
		self.lahjojen_yhteispaino += lahja.paino


	def yhteispaino(self):
		return self.lahjojen_yhteispaino



if __name__ == "__main__":
	kirja = Lahja("Aapiskukko", 2)

	pakkaus = Pakkaus()
	pakkaus.lisaa_lahja(kirja)
	print(pakkaus.yhteispaino())

	cd_levy = Lahja("Pink Floyd: Dark side of the moon", 1)
	pakkaus.lisaa_lahja(cd_levy)
	print(pakkaus.yhteispaino())
