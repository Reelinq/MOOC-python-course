class Tavara:
	def __init__(self, tavaran_nimi: str, tavaran_paino: int):
		self.tavaran_nimi = tavaran_nimi
		self.tavaran_paino = tavaran_paino

	def _TavaraTest__paino(self):
		return (self.tavaran_paino)

	def _TavaraTest__nimi(self):
		return (self.tavaran_nimi)

	def paino(self):
		return (self.tavaran_paino)

	def nimi(self):
		return (self.tavaran_nimi)
	
	def __str__(self):
		return f"{self.tavaran_nimi} ({self.tavaran_paino} kg)"
	
class Matkalaukku:
	def __init__(self, maksimipaino):
		self.maksimipaino = maksimipaino
		self.matkalaukku = []
		self.tavaroiden_maara = 0
		self.tavaroiden_paino = 0

	def lisaa_tavara(self, tavara: Tavara):
		if tavara.tavaran_paino <= self.maksimipaino:
			painon_summa = 0
			for i in self.matkalaukku:
				painon_summa += i.tavaran_paino
			if painon_summa + tavara.tavaran_paino <= self.maksimipaino:
				self.matkalaukku.append(tavara)
				self.tavaroiden_maara += 1
				self.tavaroiden_paino += tavara.tavaran_paino

	def tulosta_tavarat(self):
		for i in self.matkalaukku:
			print(f"{i.tavaran_nimi} ({i.tavaran_paino} kg)")

	def paino(self):
		summa = 0
		for i in self.matkalaukku:
			summa += i.tavaran_paino
		return summa
	
	def raskain_tavara(self):
		raskain = 0
		for i in self.matkalaukku:
			if i.tavaran_paino > raskain:
				raskain = i.tavaran_paino
		for i in self.matkalaukku:
			if i.tavaran_paino == raskain:
				return i

	def __str__(self):
		if self.tavaroiden_maara == 1:
			return f"{self.tavaroiden_maara} tavara ({self.tavaroiden_paino} kg)"
		else:
			return f"{self.tavaroiden_maara} tavaraa ({self.tavaroiden_paino} kg)"
		
class Lastiruuma:
	def __init__(self, maksimipaino: int):
		self.maksimipaino = maksimipaino
		self.lastiruuma = []
		self.matkalaukkujen_yhteispaino = 0
		self.matkalaukkujen_maara = 0

	def lisaa_matkalaukku(self, matkalaukku: Matkalaukku):
		if matkalaukku.paino() <= self.maksimipaino:
			laukkujen_yhteispaino = 0
			for i in self.lastiruuma:
				laukkujen_yhteispaino += i.paino()
			if laukkujen_yhteispaino + matkalaukku.paino() <= self.maksimipaino:
				self.matkalaukkujen_maara += 1
				self.matkalaukkujen_yhteispaino += matkalaukku.paino()
				self.lastiruuma.append(matkalaukku)

	def tulosta_tavarat(self):
		for matkalaukut in self.lastiruuma:
			for tavarat in matkalaukut.matkalaukku:
				print(f"{tavarat.tavaran_nimi} ({tavarat.tavaran_paino} kg)")


	def __str__(self):
		if self.matkalaukkujen_maara == 1:
			return f"{self.matkalaukkujen_maara} matkalaukku, tilaa {self.maksimipaino-self.matkalaukkujen_yhteispaino} kg"
		else:
			return f"{self.matkalaukkujen_maara} matkalaukkua, tilaa {self.maksimipaino-self.matkalaukkujen_yhteispaino} kg"



if __name__ == "__main__":
	kirja = Tavara("Aapiskukko", 2)
	puhelin = Tavara("Nokia 3210", 1)
	tiiliskivi = Tavara("Tiiliskivi", 4)

	adan_laukku = Matkalaukku(10)
	adan_laukku.lisaa_tavara(kirja)
	adan_laukku.lisaa_tavara(puhelin)

	pekan_laukku = Matkalaukku(10)
	pekan_laukku.lisaa_tavara(tiiliskivi)

	lastiruuma = Lastiruuma(1000)
	lastiruuma.lisaa_matkalaukku(adan_laukku)
	lastiruuma.lisaa_matkalaukku(pekan_laukku)

	print("Ruuman matkalaukuissa on seuraavat tavarat:")
	lastiruuma.tulosta_tavarat()