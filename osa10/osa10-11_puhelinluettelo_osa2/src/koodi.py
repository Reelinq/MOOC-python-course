class Henkilo:
	def __init__(self, nimi: str):
		self.henkilon_nimi = nimi
		self.henkilon_numerot = []
		self.henkilon_osoite = None

	def lisaa_numero(self, numero: str):
		self.henkilon_numerot.append(numero)

	def lisaa_osoite(self, osoite: str):
		self.henkilon_osoite = osoite
	
	def nimi(self):
		return self.henkilon_nimi
	
	def numerot(self):
		return self.henkilon_numerot
	
	def osoite(self):
		return self.henkilon_osoite

class Puhelinluettelo:
	def __init__(self):
		self.__henkilot = {}

	def lisaa_numero(self, nimi: str, numero: str):
		if not nimi in self.__henkilot:
			self.__henkilot[nimi] = Henkilo(nimi)
		self.__henkilot[nimi].lisaa_numero(numero)

	def lisaa_osoite(self, nimi: str, osoite: str):
		if not nimi in self.__henkilot:
			self.__henkilot[nimi] = Henkilo(nimi)
		self.__henkilot[nimi].lisaa_osoite(osoite)

	def hae_tiedot(self, nimi: str):
		if not nimi in self.__henkilot:
			return None
		return self.__henkilot[nimi]

	def kaikki_tiedot(self):
		return self.__henkilot

class PuhelinluetteloSovellus:
	def __init__(self):
		self.__luettelo = Puhelinluettelo()

	def ohje(self):
		print("komennot: ")
		print("0 lopetus")
		print("1 numeron lisäys")
		print("2 haku")
		print("3 osoitteen lisäys")

	def numeron_lisays(self):
		nimi = input("nimi: ")
		numero = input("numero: ")
		self.__luettelo.lisaa_numero(nimi, numero)

	def osoitteen_lisays(self):
		nimi = input("nimi: ")
		osoite = input("osoite: ")
		self.__luettelo.lisaa_osoite(nimi, osoite)

	def haku(self):
		nimi = input("nimi: ")
		if self.__luettelo.hae_tiedot(nimi) == None:
			print("osoite ei tiedossa")
			print("numero ei tiedossa")
			return
		numerot = self.__luettelo.hae_tiedot(nimi).henkilon_numerot
		if numerot == []:
			print("numero ei tiedossa")
		for numero in numerot:
			print(numero)
		osoite = self.__luettelo.hae_tiedot(nimi).henkilon_osoite
		if osoite == None:
			print("osoite ei tiedossa")
		print(osoite)

	def suorita(self):
		self.ohje()
		while True:
			print("")
			komento = input("komento: ")
			if komento == "0":
				break
			elif komento == "1":
				self.numeron_lisays()
			elif komento == "2":
				self.haku()
			elif komento == "3":
				self.osoitteen_lisays()
			else:
				self.ohje()

# kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit
sovellus = PuhelinluetteloSovellus()
sovellus.suorita()
