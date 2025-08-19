class Kurssi:
	def __init__(self, kurssin_nimi: str):
		self.kurssin_nimi = kurssin_nimi
		self.kurssin_arvosana = None
		self.kurssin_opintopisteet = None

	def lisaa_suoritus(self, arvosana: str, opintopisteet: str):
		self.kurssin_arvosana = arvosana
		self.kurssin_opintopisteet = opintopisteet

class KurssiLuettelo:
	def __init__(self):
		self.kurssiluettelo = {}

	def suorituksen_lisays(self, nimi: str, arvosana: str, opintopisteet: str):
		if nimi not in self.kurssiluettelo:
			self.kurssiluettelo[nimi] = Kurssi(nimi)
			self.kurssiluettelo[nimi].lisaa_suoritus(arvosana, opintopisteet)
		elif self.kurssiluettelo[nimi].kurssin_arvosana < arvosana:
			self.kurssiluettelo[nimi].lisaa_suoritus(arvosana, opintopisteet)

	def suorituksen_haku(self, nimi: str):
		if nimi not in self.kurssiluettelo:
			return None
		return self.kurssiluettelo[nimi]



class KurssiLuetteloSovellus:
	def __init__(self):
		self.luettelo = KurssiLuettelo()

	def ohje(self):
		print("1 lisää suoritus")
		print("2 hae suoritus")
		print("3 tilastot")
		print("0 lopetus")

	def suorituksen_lisays(self):
		kurssi = input("Kurssi: ")
		arvosana = input("Arvosana: ")
		opintopisteet = input("Opintopisteet: ")
		self.luettelo.suorituksen_lisays(kurssi, arvosana, opintopisteet)

	def suorituksen_haku(self):
		kurssi = input("Kurssi: ")
		if self.luettelo.suorituksen_haku(kurssi) == None:
			print("ei suoritusta")
		else:
			arvosana = self.luettelo.suorituksen_haku(kurssi).kurssin_arvosana
			opintopisteet = self.luettelo.suorituksen_haku(kurssi).kurssin_opintopisteet
			print(f"{kurssi} ({opintopisteet} op) arvosana {arvosana}")

	def tilaston_kirjoitus(self):
		suoritusten_maara = len(self.luettelo.kurssiluettelo)
		op_summa = 0
		arv_summa = 0
		for i in self.luettelo.kurssiluettelo.values():
			op_summa += int(i.kurssin_opintopisteet)
		for i in self.luettelo.kurssiluettelo.values():
			arv_summa += int(i.kurssin_arvosana)
		if suoritusten_maara > 0:
			keskiarvo = arv_summa / suoritusten_maara
			if keskiarvo % 1 != 0:
				keskiarvo = "{:.1f}".format(keskiarvo)
		else:
			keskiarvo = 0
		arvosanat = []
		for i in self.luettelo.kurssiluettelo.values():
			arvosanat.append(int(i.kurssin_arvosana))
		lasku_5  = "x" * arvosanat.count(5)
		lasku_4  = "x" * arvosanat.count(4)
		lasku_3  = "x" * arvosanat.count(3)
		lasku_2  = "x" * arvosanat.count(2)
		lasku_1  = "x" * arvosanat.count(1)
		
		print(f"suorituksia {suoritusten_maara} kurssilta, yhteensä {op_summa} opintopistettä")
		print(f"keskiarvo {keskiarvo}")
		print("arvosanajakauma")
		print("5: " + lasku_5)
		print("4: " + lasku_4)
		print("3: " + lasku_3)
		print("2: " + lasku_2)
		print("1: " + lasku_1)

	def suoritus(self):
		self.ohje()
		while True:
			print("")
			komento = input("Komento: ")
			if komento == "0":
				break
			elif komento == "1":
				self.suorituksen_lisays()
			elif komento == "2":
				self.suorituksen_haku()
			elif komento == "3":
				self.tilaston_kirjoitus()
			else:
				self.ohje()

sovellus = KurssiLuetteloSovellus()
sovellus.suoritus()