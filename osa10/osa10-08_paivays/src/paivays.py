class Paivays:
	def __init__(self, paiva: int, kuukausi: int, vuosi: int):
		self.paiva = paiva
		self.kuukausi = kuukausi
		self.vuosi = vuosi
		self.paivamaara = f"{self.paiva}.{self.kuukausi}.{self.vuosi}"
		self.luku = "{0:00}{1:02}{2:02}".format(self.vuosi, self.kuukausi, self.paiva)

	def __str__(self):
		return f"{self.paiva}.{self.kuukausi}.{self.vuosi}"

	def __lt__(self, toinen):
		return self.luku < toinen.luku
	
	def __gt__(self, toinen):
		return self.luku > toinen.luku

	def __eq__(self, toinen):
		return self.paivamaara == toinen.paivamaara
	
	def __ne__(self, toinen):
		return self.paivamaara != toinen.paivamaara

	def __add__(self, luku: int):
		paiva = self.paiva + luku
		kuukausi = self.kuukausi
		vuosi = self.vuosi
		if luku == 30:
			kuukausi += 1
			paiva = self.paiva
		elif paiva > 30:
			jako = paiva // 30
			paiva = paiva - (jako * 30)
			if jako + self.kuukausi > 12:
				jako2 = (jako + self.kuukausi) // 12
				kuukausi = jako + self.kuukausi - (jako2 * 12)
				vuosi = self.vuosi + jako2
			else:
				kuukausi += jako
		vastaus = Paivays(paiva, kuukausi, vuosi)
		return vastaus
	
	def __sub__(self, toinen):
		vastaus = 0
		paivamaara = self.paivamaara.split(".")
		toinen_pvm = str(toinen).split(".")
		vuosi = int(toinen_pvm[2]) - int(paivamaara[2])
		vastaus += (vuosi * 360)
		kuukausi = int(toinen_pvm[1]) - int(paivamaara[1])
		vastaus += (kuukausi * 30)
		paiva = int(toinen_pvm[0]) - int(paivamaara[0])
		vastaus += paiva
		if vastaus < 0:
			vastaus *= -1
		return vastaus

if __name__ == "__main__":
	p1 = Paivays(4, 10, 2020)
	p2 = Paivays(2, 11, 2020)
	p3 = Paivays(28, 12, 1985)

	print(p2-p1)
	print(p1-p2)
	print(p1-p3)
