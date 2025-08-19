import json


class Pelaaja:
	def __init__(self, nimi: str, kansalaisuus: str, avustukset: int, maalit: int, rangaistuspotkuja: int, joukkue: str, pelit: int):
		self.nimi = nimi
		self.kansalaisuus = kansalaisuus
		self.avustukset = avustukset
		self.maalit = maalit
		self.rangaistuspotkuja = rangaistuspotkuja
		self.joukkue = joukkue
		self.pelit = pelit
		self.pisteet = self.maalit + self.avustukset

	def __str__(self):
		return f"{self.kuvaus} ({self.tyomaara} tuntia), koodari {self.koodari} {self.onko_tehtava_valmis}"

	def on_valmis(self):
		return False if self.onko_tehtava_valmis == "EI VALMIS" else True

	def merkkaa_valmiiksi(self):
		self.onko_tehtava_valmis = "VALMIS"


class Pelaajat:
	def __init__(self):
		self.pelaajat = {}

	def lisaa_pelaaja(self, nimi: str, kansalaisuus: str, avustukset: int, maalit: int, rangaistuspotkuja: int, joukkue: str, pelit: int):
		self.pelaajat[nimi] = Pelaaja(
			nimi, kansalaisuus, avustukset, maalit, rangaistuspotkuja, joukkue, pelit)


class Sovellus:
	def __init__(self):
		self.pelaajat = Pelaajat()

	def tiedoston_luku(self):
		anto = input("tiedosto: ")
		with open(anto) as tiedosto:
			data = tiedosto.read()
		for pelaaja in json.loads(data):
			self.pelaajat.lisaa_pelaaja(pelaaja["name"], pelaaja["nationality"], pelaaja["assists"],
			                            pelaaja["goals"], pelaaja["penalties"], pelaaja["team"], pelaaja["games"])

	def ohje(self):
		print("komennot:")
		print("0 lopeta")
		print("1 hae pelaaja")
		print("2 joukkueet")
		print("3 maat")
		print("4 joukkuen pelaajat")
		print("5 maan pelaajat")
		print("6 eniten pisteitä")
		print("7 eniten maaleja")

	def pelaajan_haku(self):
		nimi = input("nimi: ")
		for pelaaja in self.pelaajat.pelaajat:
			if pelaaja == nimi:
				pelaaja_data = self.pelaajat.pelaajat[pelaaja]
				print(f"{nimi:20} {pelaaja_data.joukkue} {pelaaja_data.maalit:>3} + {pelaaja_data.avustukset:>2} = {pelaaja_data.maalit + pelaaja_data.avustukset:>3}")

	def joukkueet(self):
		joukkueet = []
		for pelaaja in self.pelaajat.pelaajat:
			joukkue = self.pelaajat.pelaajat[pelaaja].joukkue
			if joukkue not in joukkueet:
				joukkueet.append(joukkue)
		for joukkue in sorted(joukkueet):
			print(joukkue)

	def maat(self):
		maat = []
		for pelaaja in self.pelaajat.pelaajat:
			maa = self.pelaajat.pelaajat[pelaaja].kansalaisuus
			if maa not in maat:
				maat.append(maa)
		for maa in sorted(maat):
			print(maa)

	def joukkueen_pelaajat(self):
		joukkue = input("joukkue: ")
		lista_joukkueesta = []
		for pelaaja in self.pelaajat.pelaajat:
			if self.pelaajat.pelaajat[pelaaja].joukkue == joukkue:
				lista_joukkueesta.append(pelaaja)
		uusi_lista = sorted(lista_joukkueesta, key=lambda x: x[-1])
		for pelaaja in uusi_lista:
			pelaaja_data = self.pelaajat.pelaajat[pelaaja]
			print(f"{pelaaja:20} {pelaaja_data.joukkue} {pelaaja_data.maalit:>3} + {pelaaja_data.avustukset:>2} = {pelaaja_data.maalit + pelaaja_data.avustukset:>3}")

	def maan_pelaajat(self):
		maa = input("maa: ")
		lista_maasta = []
		for pelaaja in self.pelaajat.pelaajat:
			if self.pelaajat.pelaajat[pelaaja].kansalaisuus == maa:
				lista_maasta.append((pelaaja, self.pelaajat.pelaajat[pelaaja].pisteet))
		uusi_lista = sorted(lista_maasta, key=lambda x: x[1], reverse=True)
		for pelaaja in uusi_lista:
			pelaaja_data = self.pelaajat.pelaajat[pelaaja[0]]
			print(f"{pelaaja[0]:20} {pelaaja_data.joukkue} {pelaaja_data.maalit:>3} + {pelaaja_data.avustukset:>2} = {pelaaja_data.maalit + pelaaja_data.avustukset:>3}")

	def eniten_pisteita(self):
		paljon = int(input("kuinka monta: "))
		lista_pisteet = []
		for pelaaja in self.pelaajat.pelaajat:
			lista_pisteet.append((pelaaja, self.pelaajat.pelaajat[pelaaja].pisteet))
		uusi_lista = sorted(lista_pisteet, key=lambda x: x[1], reverse=True)
		for pelaaja in uusi_lista[:paljon]:
			pelaaja_data = self.pelaajat.pelaajat[pelaaja[0]]
			print(f"{pelaaja[0]:20} {pelaaja_data.joukkue} {pelaaja_data.maalit:>3} + {pelaaja_data.avustukset:>2} = {pelaaja_data.maalit + pelaaja_data.avustukset:>3}")

	def eniten_maaleja(self):
		paljon = int(input("kuinka monta: "))
		lista_pisteet = []
		for pelaaja in self.pelaajat.pelaajat:
			lista_pisteet.append(
				(pelaaja, self.pelaajat.pelaajat[pelaaja].maalit, self.pelaajat.pelaajat[pelaaja].pelit))
		uusi_lista = sorted(lista_pisteet, key=lambda x: (-x[1], x[2]))
		for pelaaja in uusi_lista[:paljon]:
			pelaaja_data = self.pelaajat.pelaajat[pelaaja[0]]
			print(f"{pelaaja[0]:20} {pelaaja_data.joukkue} {pelaaja_data.maalit:>3} + {pelaaja_data.avustukset:>2} = {pelaaja_data.maalit + pelaaja_data.avustukset:>3}")

	def suoritus(self):
		self.tiedoston_luku()
		pelaajien_maara = len(self.pelaajat.pelaajat)
		print(f"luettiin {pelaajien_maara} pelaajan tiedot")
		print(f"4 joukkueen pelaajat")
		print("")
		self.ohje()
		while True:
			print("")
			komento = input("Komento: ")
			if komento == "0":
				break
			elif komento == "1":
				self.pelaajan_haku()
			elif komento == "2":
				self.joukkueet()
			elif komento == "3":
				self.maat()
			elif komento == "4":
				self.joukkueen_pelaajat()
			elif komento == "5":
				self.maan_pelaajat()
			elif komento == "6":
				self.eniten_pisteita()
			elif komento == "7":
				self.eniten_maaleja()
			else:
				self.ohje()

sovellus = Sovellus()
sovellus.suoritus()