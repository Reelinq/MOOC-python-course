import random

class Sanapeli():
	def __init__(self, kierrokset: int):
		self.voitot1 = 0
		self.voitot2 = 0
		self.kierrokset = kierrokset

	def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
		# arvotaan voittaja
		return random.randint(1, 2)

	def pelaa(self):
		print("Sanapeli:")
		for i in range(1, self.kierrokset+1):
			print(f"kierros {i}")
			vastaus1 = input("pelaaja1: ")
			vastaus2 = input("pelaaja2: ")

			if self.kierroksen_voittaja(vastaus1, vastaus2) == 1:
				self.voitot1 += 1
				print("pelaaja 1 voitti")
			elif self.kierroksen_voittaja(vastaus1, vastaus2) == 2:
				self.voitot2 += 1
				print("pelaaja 2 voitti")
			else:
				pass # tasapeli

		print("peli päättyi, voitot:")
		print(f"pelaaja 1: {self.voitot1}")
		print(f"pelaaja 2: {self.voitot2}")


class PisinSana(Sanapeli):
	def __init__(self, kierrokset: int):
		super().__init__(kierrokset)

	def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
		if len(pelaaja1_sana) > len(pelaaja2_sana):
			return 1
		if len(pelaaja1_sana) < len(pelaaja2_sana):
			return 2

class EnitenVokaaleja(Sanapeli):
	def __init__(self, kierrokset: int):
		super().__init__(kierrokset)

	def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
		vokaalit = "aeiouyäöAEIOUYÄÖ"
		summa1 = 0
		summa2 = 0
		for kirjain in pelaaja1_sana:
			if kirjain in vokaalit:
				summa1 += 1
		for kirjain in pelaaja2_sana:
			if kirjain in vokaalit:
				summa2 += 1
		if summa1 > summa2:
			return 1
		if summa1 < summa2:
			return 2

class KiviPaperiSakset(Sanapeli):
	def __init__(self, kierrokset: int):
		super().__init__(kierrokset)

	def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
		if pelaaja1_sana == "kivi" and pelaaja2_sana == "paperi":
			return 2
		elif pelaaja1_sana == "kivi" and pelaaja2_sana == "sakset":
			return 1
		elif pelaaja1_sana == "sakset" and pelaaja2_sana == "paperi":
			return 1
		elif pelaaja1_sana == "sakset" and pelaaja2_sana == "kivi":
			return 2
		elif pelaaja1_sana == "paperi" and pelaaja2_sana == "kivi":
			return 1
		elif pelaaja1_sana == "paperi" and pelaaja2_sana == "sakset":
			return 2
		elif pelaaja1_sana == pelaaja2_sana:
			pass
		elif pelaaja1_sana not in ["kivi", "paperi", "sakset"] and pelaaja2_sana not in ["kivi", "paperi", "sakset"]:
			pass
		elif pelaaja1_sana not in ["kivi", "paperi", "sakset"]:
			return 2
		elif pelaaja2_sana not in ["kivi", "paperi", "sakset"]:
			return 1

if __name__ == "__main__":
	p = PisinSana(3)
	p.pelaa()


