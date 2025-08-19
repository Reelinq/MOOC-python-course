class Henkilo:
	def __init__(self, nimi: str, pituus: int):
		self.nimi = nimi
		self.pituus = pituus

	def __str__(self):
		return self.nimi
	
class Huone:
	def __init__(self):
		self.henkilot = []
		self.henkilo_maara = 0
		self.henkiloiden_pituus = 0

	def lisaa(self, henkilo: Henkilo):
		self.henkilot.append(henkilo)
		self.henkilo_maara += 1
		self.henkiloiden_pituus += henkilo.pituus

	def on_tyhja(self):
		if self.henkilot == []:
			return True
		else:
			return False

	def tulosta_tiedot(self):
		print(f"Huoneessa {self.henkilo_maara} henkiöä, yhteispituus {self.henkiloiden_pituus} cm")
		for hlo in self.henkilot:
			print(f"{hlo.nimi} ({hlo.pituus} cm)")

	def lyhin(self):
		hlot = []
		for hlo in self.henkilot:
			hlot.append(hlo.pituus)
		for hlo in self.henkilot:
			if hlo.pituus == min(hlot):
				return hlo
			
	def poista_lyhin(self):
		lyhin_henkilo = self.lyhin()
		if lyhin_henkilo:
			self.henkilot.remove(lyhin_henkilo)
			self.henkilo_maara -= 1
			self.henkiloiden_pituus -= lyhin_henkilo.pituus
			return lyhin_henkilo
		else:
			return None

if __name__ == "__main__":

	huone = Huone()

	huone.lisaa(Henkilo("Anu", 120))
	huone.lisaa(Henkilo("Pena", 150))

	poistettu = huone.poista_lyhin()
	print(f"Otettiin huoneesta {poistettu.nimi}")
	huone.tulosta_tiedot()