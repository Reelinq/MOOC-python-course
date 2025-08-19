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
		return f"{self.id}: {self.kuvaus} ({self.tyomaara} tuntia), koodari {self.koodari} {self.onko_tehtava_valmis}"

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
			raise ValueError("Tehtävää ei löydy")
		for tilaus in self.tilaukset:
			if tilaus.id == id:
				tilaus.merkkaa_valmiiksi()
			
			
	def valmiit_tilaukset(self):
		return [tilaus for tilaus in self.tilaukset if tilaus.onko_tehtava_valmis == "VALMIS"]

	def ei_valmiit_tilaukset(self):
		return [tilaus for tilaus in self.tilaukset if tilaus.onko_tehtava_valmis == "EI VALMIS"]
	
	def koodarin_status(self, koodari: str):
		koodarin_tilaukset = [tilaus for tilaus in self.tilaukset if tilaus.koodari == koodari]
		if koodarin_tilaukset == []:
			raise ValueError("Koodaria ei löytynyt")
		valmiit = [tilaus.tyomaara for tilaus in koodarin_tilaukset if tilaus.onko_tehtava_valmis == "VALMIS"]
		ei_valmiit = [tilaus.tyomaara for tilaus in koodarin_tilaukset if tilaus.onko_tehtava_valmis == "EI VALMIS"]
		return len(valmiit), len(ei_valmiit), sum(valmiit), sum(ei_valmiit)