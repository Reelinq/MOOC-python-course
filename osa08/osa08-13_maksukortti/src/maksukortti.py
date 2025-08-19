class Maksukortti:
	def __init__(self, alkusaldo: float):
		self.saldo = alkusaldo

	def syo_edullisesti(self):
		if self.saldo >= 2.6:
			self.saldo -= 2.6
	
	def syo_maukkaasti(self):
		if self.saldo >= 4.6:
			self.saldo -= 4.6

	def lataa_rahaa(self, lataus_summa: int):
		if lataus_summa > 0:
			self.saldo += lataus_summa
		else:
			virhe = ValueError("Kortille ei saa ladata negatiivista summaa")
			raise virhe

	def __str__(self):
		return f"Kortilla on rahaa {self.saldo:.1f} euroa"

pekan_kortti = Maksukortti(20)
matin_kortti = Maksukortti(30)
pekan_kortti.syo_maukkaasti()
matin_kortti.syo_edullisesti()
print("Pekka:", pekan_kortti)
print("Matti:", matin_kortti)
pekan_kortti.lataa_rahaa(20)
matin_kortti.syo_maukkaasti()
print("Pekka:", pekan_kortti)
print("Matti:", matin_kortti)
pekan_kortti.syo_edullisesti()
pekan_kortti.syo_edullisesti()
matin_kortti.lataa_rahaa(50)
print("Pekka:", pekan_kortti)
print("Matti:", matin_kortti)