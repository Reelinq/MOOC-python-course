class Tehtava:
	vika_id = 0

	def __init__(self, kuvaus: str, koodari: str, tyomaara: int):
		Tehtava.vika_id += 1
		self.kuvaus = kuvaus
		self.koodari = koodari
		self.tyomaara = tyomaara
		self.onko_tehtava_valmis = "EI VALMIS"
		self.id = Tehtava.vika_id

	def __str__(self):
		return f"{self.kuvaus} ({self.tyomaara} tuntia), koodari {self.koodari} {self.onko_tehtava_valmis}"

	def on_valmis(self):
		return False if self.onko_tehtava_valmis == "EI VALMIS" else True

	def merkkaa_valmiiksi(self):
		self.onko_tehtava_valmis = "VALMIS"


class Tilauskirja:
	def __init__(self):
		self.tilaukset = []

	def lisaa_tilaus(self, kuvaus: str, koodari: str, tyomaara: int):
		self.tilaukset.append(Tehtava(kuvaus, koodari, tyomaara))

	def kaikki_tilaukset(self):
		return self.tilaukset

	def koodarit(self):
		return list(set([tilaus.koodari for tilaus in self.tilaukset]))

	def merkkaa_valmiiksi(self, id: int):
		id_lista = [tilaus.id for tilaus in self.tilaukset]
		if id not in id_lista:
			return "virheellinen syöte"
		for tilaus in self.tilaukset:
			if tilaus.id == id:
				tilaus.merkkaa_valmiiksi()

	def valmiit_tilaukset(self):
		return [tilaus for tilaus in self.tilaukset if tilaus.onko_tehtava_valmis == "VALMIS"]

	def ei_valmiit_tilaukset(self):
		return [tilaus for tilaus in self.tilaukset if tilaus.onko_tehtava_valmis == "EI VALMIS"]

	def koodarin_status(self, koodari: str):
		koodarin_tilaukset = [
			tilaus for tilaus in self.tilaukset if tilaus.koodari == koodari]
		if koodarin_tilaukset == []:
			return False
		valmiit = [
			tilaus.tyomaara for tilaus in koodarin_tilaukset if tilaus.onko_tehtava_valmis == "VALMIS"]
		ei_valmiit = [
			tilaus.tyomaara for tilaus in koodarin_tilaukset if tilaus.onko_tehtava_valmis == "EI VALMIS"]
		return len(valmiit), len(ei_valmiit), sum(valmiit), sum(ei_valmiit)
	
class Sovellus:
	def __init__(self):
		self.tilauskirja = Tilauskirja()

	def ohje(self):
		print("komennot:")
		print("0 lopetus")
		print("1 lisää tilaus")
		print("2 listaa valmiit")
		print("3 listaa ei valmiit")
		print("4 merkitse tehtävä valmiiksi")
		print("5 koodarit")
		print("6 koodarin status")

	def tilauksen_lisays(self):
		kuvaus = input("kuvaus: ")
		valiarvo = input("koodari ja työmääräarvio: ")
		uusi_valiarvo = valiarvo.split()
		koodari = uusi_valiarvo[0]
		try:
			int(uusi_valiarvo[1])
		except:
			print("virheellinen syöte")
			return
		print("lisätty!")
		tyomaaraarvio = int(uusi_valiarvo[1])
		self.tilauskirja.lisaa_tilaus(kuvaus, koodari, tyomaaraarvio)

	def listaa_valmiit(self):
		if self.tilauskirja.valmiit_tilaukset() == []:
			print("ei valmiita")
		else:
			for tilaus in self.tilauskirja.valmiit_tilaukset():
				print(tilaus)

	def listaa_ei_valmiit(self):
		ei_valmiit = self.tilauskirja.ei_valmiit_tilaukset()
		if not ei_valmiit:
			print("ei tilauksia")
		else:
			for tilaus in ei_valmiit:
				print(tilaus)

	def merkitse_valmiiksi(self):
		tunniste = input("tunniste: ")
		try:
			int(tunniste)
		except:
			print("virheellinen syöte")
			return
		if self.tilauskirja.merkkaa_valmiiksi(int(tunniste)) == "virheellinen syöte":
			print("virheellinen syöte")
		else:
			self.tilauskirja.merkkaa_valmiiksi(int(tunniste))
			print("merkitty valmiiksi")

	def koodarit(self):
		for tilaus in self.tilauskirja.koodarit():
			print(tilaus)

	def koodarin_status(self):
		koodari = input("koodari: ")
		vastaus = self.tilauskirja.koodarin_status(koodari)
		if vastaus == False:
			print("virheellinen syöte")
			return
		print(f"työt: valmiina {vastaus[0]} ei valmiina {vastaus[1]}, tunteja: tehty {vastaus[2]} tekemättä {vastaus[3]}")

	def suoritus(self):
		self.ohje()
		while True:
			print("")
			komento = input("Komento: ")
			if komento == "0":
				break
			elif komento == "1":
				self.tilauksen_lisays()
			elif komento == "2":
				self.listaa_valmiit()
			elif komento == "3":
				self.listaa_ei_valmiit()
			elif komento == "4":
				self.merkitse_valmiiksi()
			elif komento == "5":
				self.koodarit()
			elif komento == "6":
				self.koodarin_status()
			else:
				self.ohje()


sovellus = Sovellus()
sovellus.suoritus()
