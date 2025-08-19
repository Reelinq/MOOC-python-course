from datetime import date, datetime, timedelta
import json
import re

osastot = [] #Luodaan tyhjä lista osastoille, johon lisätään osastot myöhemmin
tyontekijat = [] #Luodaan tyhjä lista työntekijöille, johon lisätään työntekijät myöhemmin
käytetyt_id = {} #Luodaan tyhjä sanakirja, johon lisätään osastojen käytetyt id:t

class Tyontekija: #Luodaan luokka Tyontekija, luokka maarittelee tyontekijan ominaisuudet
	def __init__(self, etunimi: str, sukunimi: str, osasto: str, tyonimike: str, sahkopostiosoite: str, kuukausipalkka: str, tyon_aloitus_pvm: date, tyontekijatunnus: str = None):
		if not tyontekijatunnus:
			self.tyontekijatunnus = self.generate_tyontekijatunnus(osasto)
		else:
			self.tyontekijatunnus = tyontekijatunnus
		self.etunimi = etunimi
		self.sukunimi = sukunimi
		self.osasto = osasto
		self.tyonimike = tyonimike
		self.sahkopostiosoite = sahkopostiosoite
		self.kuukausipalkka = kuukausipalkka
		self.tyon_aloitus_pvm = tyon_aloitus_pvm


	@staticmethod
	def generate_tyontekijatunnus(osasto): #Luodaan metodi, joka luo työntekijätunnuksen
		osaston_lyhenne = osasto.split(":")[0]
		if osaston_lyhenne not in käytetyt_id:
			käytetyt_id[osaston_lyhenne] = 1
		else:
			käytetyt_id[osaston_lyhenne] += 1

		return f"{osaston_lyhenne}{käytetyt_id[osaston_lyhenne]:03d}"



class Esihenkilokunta(Tyontekija): #Luodaan luokka Esihenkilokunta, joka perii luokan Tyontekija ominaisuudet
	def __init__(self, etunimi: str, sukunimi: str, osasto: str, tyonimike: str, sahkopostiosoite: str, kuukausipalkka: str, tyon_aloitus_pvm: date, alaiset: list, tyontekijatunnus: str = None):
		super().__init__(etunimi, sukunimi, osasto, tyonimike, sahkopostiosoite, kuukausipalkka, tyon_aloitus_pvm, tyontekijatunnus)
		self.alaiset = alaiset



class OhjelmanKaynistys: #Luodaan luokka OhjelmanKaynnistys, joka maarittelee ohjelman kaynnistyksen ominaisuudet
	def lataa_tyontekijat_jsonista(self): #Luodaan metodi, joka lataa työntekijät JSON-tiedostosta
		with open('henkilot.json', 'r') as file:
			data = json.load(file)
			for tyontekijan_tiedot in data:
				alaiset = tyontekijan_tiedot.get('alaiset', [])
				valmiit_alaiset = []
				for alainen in alaiset:
					for tyontekija in data:
						if tyontekija.get('tyontekijatunnus') == alainen:
							tyontekijan_class = Tyontekija(
								tyontekija.get('etunimi'),
								tyontekija.get('sukunimi'),
								tyontekija.get('osasto'),
								tyontekija.get('tyonimike'),
								tyontekija.get('sahkopostiosoite'),
								tyontekija.get('kuukausipalkka'),
								date.fromisoformat(tyontekija.get('tyon_aloitus_pvm')),
								tyontekija.get('tyontekijatunnus')
							)
							valmiit_alaiset.append(tyontekijan_class)
				
				if valmiit_alaiset: #Jos alaisia on, luodaan Esihenkilokunta-olio
					uusi_tyontekija = Esihenkilokunta(
						tyontekijan_tiedot.get('etunimi'),
						tyontekijan_tiedot.get('sukunimi'),
						tyontekijan_tiedot.get('osasto'),
						tyontekijan_tiedot.get('tyonimike'),
						tyontekijan_tiedot.get('sahkopostiosoite'),
						tyontekijan_tiedot.get('kuukausipalkka'),
						date.fromisoformat(tyontekijan_tiedot.get('tyon_aloitus_pvm')),
						valmiit_alaiset,
						tyontekijan_tiedot.get('tyontekijatunnus')
					)
				else: #Jos alaisia ei ole, luodaan Tyontekija-olio
					uusi_tyontekija = Tyontekija(
						tyontekijan_tiedot.get('etunimi'),
						tyontekijan_tiedot.get('sukunimi'),
						tyontekijan_tiedot.get('osasto'),
						tyontekijan_tiedot.get('tyonimike'),
						tyontekijan_tiedot.get('sahkopostiosoite'),
						tyontekijan_tiedot.get('kuukausipalkka'),
						date.fromisoformat(tyontekijan_tiedot.get('tyon_aloitus_pvm')),
						tyontekijan_tiedot.get('tyontekijatunnus')
					)
				tyontekijat.append({uusi_tyontekija.tyontekijatunnus: uusi_tyontekija}) #Lisätään työntekijä listaan


	def lataa_kaytetyt_id(self): #Luodaan metodi, joka lataa käytetyt id:t JSON-tiedostosta
		with open('henkilot.json', 'r') as file:
			data = json.load(file)
			for tyontekijan_tiedot in data:
				match = re.match(r"([a-z]+)([0-9]+)", tyontekijan_tiedot['tyontekijatunnus'], re.I)
				if match:
					osasto = list(match.groups())[0] #Otetaan osasto talteen
					tyontekijatunnus = int(list(match.groups())[1]) #Otetaan työntekijätunnus talteen
				if osasto not in käytetyt_id or tyontekijatunnus > käytetyt_id[osasto]: 
					käytetyt_id[osasto] = tyontekijatunnus #Jos osastoa ei ole käytetty tai työntekijätunnus on suurempi kuin käytetty, lisätään käytettyyn id:hen



class OsastojenKasitys: #Luodaan luokka OsastojenKasitys, joka maarittelee osastojen käsittelyn ominaisuudet
	def lataa_osastot(self): #Luodaan metodi, joka lataa osastot JSON-tiedostosta
		with open('henkilot.json', 'r') as file:
			data = json.load(file)
			for tyontekija in data:
				osasto = tyontekija["osasto"]
				if osasto not in osastot:
					osastot.append(osasto)


	def osaston_tarkistus(self, osasto): #Luodaan metodi, joka tarkistaa osaston oikeellisuuden
		if ":" not in osasto:
			print("Virheellinen syöte")
			return False

		osaston_lyhenne = osasto.split(":")[0]
		osaston_nimi = osasto.split(":")[1]

		valid = True

		if osaston_lyhenne == "":
			print("Osaston lyhenne puuttuu")
			valid = False
		elif osaston_nimi == "":
			print("Osaston nimi puuttuu")
			valid = False
		elif osaston_lyhenne not in osaston_lyhenne.upper():
			print("Osaston lyhenne pitää olla isoilla kirjaimilla")
			valid = False
		elif len(osaston_lyhenne) != 4:
			print("Osaston lyhenteen pituus pitää olla 4 merkkiä")
			valid = False
		elif osasto in osastot:
			print("Osasto on jo olemassa")
			valid = False

		if valid:
			return True
		else:
			return False



class TyontkijoidenKasitys: #Luodaan luokka TyontekijoidenKasitys, joka maarittelee työntekijöiden käsittelyn ominaisuudet
	def lisaa_tyontekija(self, etunimi: str, sukunimi: str, osasto: str, tyonimike: str, sahkopostiosoite: str, kuukausipalkka: str, tyon_aloitus_pvm: date): #Luodaan metodi, joka lisää työntekijän
		uusi_tyontekija = Tyontekija(etunimi, sukunimi, osasto, tyonimike, sahkopostiosoite, kuukausipalkka, tyon_aloitus_pvm)
		tyontekijat.append({uusi_tyontekija.tyontekijatunnus: uusi_tyontekija})
		self.tallenna_json_tiedostoon(uusi_tyontekija)


	def tallenna_json_tiedostoon(self, tyontekija: Tyontekija): #Luodaan metodi, joka tallentaa lisätyn työntekijän JSON-tiedostoon
		with open('henkilot.json', 'r') as file:
			data = json.load(file)
		data.append({
			"tyontekijatunnus": tyontekija.tyontekijatunnus,
			"etunimi": tyontekija.etunimi,
			"sukunimi": tyontekija.sukunimi,
			"osasto": tyontekija.osasto,
			"tyonimike": tyontekija.tyonimike,
			"sahkopostiosoite": tyontekija.sahkopostiosoite,
			"kuukausipalkka": tyontekija.kuukausipalkka,
			"tyon_aloitus_pvm": tyontekija.tyon_aloitus_pvm
		})
		with open('henkilot.json', 'w') as file:
			json.dump(data, file, ensure_ascii=False, indent=4)


	def esihenkilokunnan_lisays(self, etunimi: str, sukunimi: str, osasto: str, tyonimike: str, sahkopostiosoite: str, kuukausipalkka: str, tyon_aloitus_pvm: date, alaiset: list): #Luodaan metodi, joka lisää esihenkilön
		uusi_tyontekija = Esihenkilokunta(etunimi, sukunimi, osasto, tyonimike, sahkopostiosoite, kuukausipalkka, tyon_aloitus_pvm, alaiset)
		tyontekijat.append({uusi_tyontekija.tyontekijatunnus: uusi_tyontekija})
		self.tallenna_esihenkilokunnan_json_tiedostoon(uusi_tyontekija)


	def tallenna_esihenkilokunnan_json_tiedostoon(self, tyontekija: Esihenkilokunta): #Luodaan metodi, joka tallentaa lisätyn esihenkilön JSON-tiedostoon
		with open('henkilot.json', 'r') as file:
			data = json.load(file)
		data.append({
			"tyontekijatunnus": tyontekija.tyontekijatunnus,
			"etunimi": tyontekija.etunimi,
			"sukunimi": tyontekija.sukunimi,
			"osasto": tyontekija.osasto,
			"tyonimike": tyontekija.tyonimike,
			"sahkopostiosoite": tyontekija.sahkopostiosoite,
			"kuukausipalkka": tyontekija.kuukausipalkka,
			"tyon_aloitus_pvm": tyontekija.tyon_aloitus_pvm,
			"alaiset": [alainen.tyontekijatunnus for alainen in tyontekija.alaiset]
		})
		with open('henkilot.json', 'w') as file:
			json.dump(data, file, ensure_ascii=False, indent=4)


	def poista_tyontekija(self, nimi_input): #Luodaan metodi, joka poistaa työntekijän
		for tyontekija_dict in tyontekijat:
			for key, value in tyontekija_dict.items():
				if value.etunimi + " " + value.sukunimi == nimi_input:
					tyontekijat.remove(tyontekija_dict) #Poistetaan työntekijä listasta

					with open('henkilot.json', 'r') as file: #Poistetaan työntekijä JSON-tiedostosta
						data = json.load(file)
					for index, tyontekija in enumerate(data):
						if tyontekija.get('etunimi') + " " + tyontekija.get('sukunimi') == nimi_input:
							del data[index]
							break
					with open('henkilot.json', 'w') as file:
						json.dump(data, file, ensure_ascii=False, indent=4)
					return


	def poista_tyontekija_tyontekijatunnuksella(self, tyontekijatunnus): #Luodaan metodi, joka poistaa työntekijän työntekijätunnuksella
		for tyontekija_dict in tyontekijat:
			for key, value in tyontekija_dict.items():
				if value.tyontekijatunnus == tyontekijatunnus:
					tyontekijat.remove(tyontekija_dict) #Poistetaan työntekijä listasta
					
					with open('henkilot.json', 'r') as file: #Poistetaan työntekijä JSON-tiedostosta
						data = json.load(file)
					for index, tyontekija in enumerate(data):
						if tyontekija.get('tyontekijatunnus') == tyontekijatunnus:
							del data[index]
							break
					with open('henkilot.json', 'w') as file:
						json.dump(data, file, ensure_ascii=False, indent=4)
					return


	def paivita_tyontekijat_json(self): #Luodaan metodi, joka päivittää työntekijät JSON-tiedostoon, jos niihin on tullut muutoksia tyontekija listassa
		with open('henkilot.json', 'r') as file:
			data = json.load(file)

		data_dict = {d['tyontekijatunnus']: d for d in data}

		for tyontekija_dict in tyontekijat:
			for key, value in tyontekija_dict.items():
				if hasattr(value, 'tyon_aloitus_pvm'): #Muutetaan päivämäärä ISO-muotoon
					value.tyon_aloitus_pvm = value.tyon_aloitus_pvm if isinstance(value.tyon_aloitus_pvm, str) else value.tyon_aloitus_pvm.isoformat() if isinstance(value.tyon_aloitus_pvm, date) else value.tyon_aloitus_pvm
				tyontekija_data = value.__dict__.copy()
				if 'alaiset' in tyontekija_data: #Vaihdetaan alaiset pelkkiin työntekijätunnukssiin
					tyontekija_data['alaiset'] = [tyontekija.tyontekijatunnus for tyontekija in tyontekija_data['alaiset']]
				if key in data_dict:
					json_tyontekija = data_dict[key]
					if json_tyontekija != tyontekija_data:
						data_dict[key] = tyontekija_data
				else:
					data_dict[key] = tyontekija_data

		updated_data = list(data_dict.values())
		with open('henkilot.json', 'w') as file:
			json.dump(updated_data, file, ensure_ascii=False, indent=4)


	def tarkista_tyontekijatunnuksen_kopiot(self): #Luodaan metodi, joka tarkistaa onko työntekijöitä, jotka esiintyvät useammin kuin kerran
		with open('henkilot.json', 'r') as file:
			data = json.load(file)

		tyontekijatunnukset = [tyontekija.get('tyontekijatunnus') for tyontekija in data]
		unique_tyontekijatunnukset = set()
		kopiot = set()

		for tyontekijatunnus in tyontekijatunnukset:
			if tyontekijatunnus in unique_tyontekijatunnukset:
				kopiot.add(tyontekijatunnus)
			else:
				unique_tyontekijatunnukset.add(tyontekijatunnus)

		if kopiot: #Jos kopioita löytyy, poistetaan ne JSON-tiedostosta
			data = [tyontekija for i, tyontekija in enumerate(data) if tyontekija['tyontekijatunnus'] not in kopiot or (kopiot.remove(tyontekija['tyontekijatunnus']) is None and True)]
			with open('henkilot.json', 'w') as file:
				json.dump(data, file, ensure_ascii=False, indent=4)
			return True



class TekninenSovellus: #Luodaan luokka TekninenSovellus, joka maarittelee teknisen sovelluksen ominaisuudet
	def __init__(self): #Luodaan luokan konstruktori
		self.ohjelman_kaynnistys = OhjelmanKaynistys()
		self.osastojen_kasitys = OsastojenKasitys()
		self.tyontekijoiden_kasitys = TyontkijoidenKasitys()


	def lisaa_osasto(self): #Luodaan metodi, joka lisää osaston
		print("Anna osasto muodossa 'lyhenne:osaston nimi'")
		print("Esim. TIKA:Tietokanta")
		osasto = input("osasto: ")
		print("")

		if self.osastojen_kasitys.osaston_tarkistus(osasto):
			osastot.append(osasto)
			print("Lisätty osasto", osasto.split(":")[0])


	def osastojen_listaus(self): #Luodaan metodi, joka listaa osastot
		for osasto in set([osasto for osasto in sorted(osastot)]):
			print(osasto)


	def tyontekijan_lisays(self): #Luodaan metodi, joka lisää työntekijän
		palautus = True

		etunimi = input("etunimi: ")
		if not re.match(r'^[a-zA-ZäöåÄÖÅ]+$', etunimi):
			print("Virheellinen etunimi")
			palautus = False
			return

		sukunimi = input("sukunimi: ")
		if not re.match(r'^[a-zA-ZäöåÄÖÅ]+$', sukunimi):
			print("Virheellinen sukunimi")
			palautus = False
			return

		osasto = input("osaston lyhenne, esim. TUKE: ")
		if len(osasto) != 4:
			print("Osaston lyhenne pitää olla 4 merkkiä pitkä")
			palautus = False
			return
		if osasto not in osasto.upper():
			print("Osaston lyhenne pitää olla isoilla kirjaimilla")
			palautus = False
			return
		if osasto not in [osasto.split(":")[0] for osasto in osastot]:
			print("Osastoa ei ole olemassa")
			palautus = False
			return
		tarvittava_osasto = ""
		for i in osastot:
			if osasto == i.split(":")[0]:
				tarvittava_osasto = i

		tyonimike = input("työnimike: ")
		if not re.match(r'^[a-zA-ZäöåÄÖÅ\s]+$', tyonimike):
			print("Virheellinen työnimike")
			palautus = False
			return

		sahkopostiosoite = input("sähköpostiosoite muodossa 'esimerkki@sahkoposti.verkkotunnus': ")
		email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
		if not re.match(email_pattern, sahkopostiosoite):
			print("Virheellinen sähköpostiosoite")
			palautus = False
			return

		kuukausipalkka = input("kuukausipalkka: ")
		if not re.match(r'^\d+(\.\d{1,2})?$', kuukausipalkka):
			print("Virheellinen kuukausipalkka")
			palautus = False
			return

		tyon_aloitus_pvm = input("työn aloitus pvm muodossa vuosi-kuukaus-päivä: ")
		try:
			aloitus_pvm = datetime.strptime(tyon_aloitus_pvm, '%Y-%m-%d')
			if aloitus_pvm > datetime.now():
				print("Päivämäärä ei voi olla tulevaisuudessa")
				palautus = False
				return
		except ValueError:
			print("Virheellinen päivämäärä")
			palautus = False
			return
		
		esihlo = False
		
		esihenkilokunta = input("Onko työntekijä esihenkilö? (k/e): ") #listään vielä pätkä, joka määrittää onko työntekijä esihenkilö
		if esihenkilokunta == "k":
			esihlo = True
			alaiset = input("Anna alaisten työntekijäntunnukset pilkulla erotettuna: ")
			alaiset = alaiset.split(",")
			valmiit_alaiset = []
			for alainen in alaiset:
				alainen = alainen.strip()
				found = False
				for tyontekija_dict in tyontekijat:
					for tyontekija in tyontekija_dict.values():
						if alainen == tyontekija.tyontekijatunnus:
							valmiit_alaiset.append(Tyontekija(
								tyontekija.etunimi,
								tyontekija.sukunimi,
								tyontekija.osasto,
								tyontekija.tyonimike,
								tyontekija.sahkopostiosoite,
								tyontekija.kuukausipalkka,
								tyontekija.tyon_aloitus_pvm,
								tyontekija.tyontekijatunnus))
							found = True
							break
					if found:
						break
				if not found:
					print(f"Alaista {alainen} ei löydy")
					palautus = False
					return
			self.tyontekijoiden_kasitys.esihenkilokunnan_lisays(etunimi, sukunimi, tarvittava_osasto, tyonimike, sahkopostiosoite, kuukausipalkka, tyon_aloitus_pvm, valmiit_alaiset)
			print("")
			print("Työntekijä lisätty!")

		if palautus:
			if esihlo == False:
				self.tyontekijoiden_kasitys.lisaa_tyontekija(etunimi, sukunimi, tarvittava_osasto, tyonimike, sahkopostiosoite, kuukausipalkka, tyon_aloitus_pvm)
				print("")
				print("Työntekijä lisätty!")


	def tyontekijan_poisto(self): #Luodaan metodi, joka poistaa työntekijän
		nimi_input = input("Anna työntekijän nimi: ")
		nimen_tiedot = [ #Tarkistetaan onko samalla nimellä useampia työntekijöitä
		tyontekija_dict for tyontekija_dict in tyontekijat
		for tyontekija in tyontekija_dict.values()
		if tyontekija.etunimi + " " + tyontekija.sukunimi == nimi_input
	]

		if len(nimen_tiedot) > 1: #Jos useampia työntekijöitä löytyy, kysytään kumpaa tarkoitetaan ja poistetaan se
			print("")
			print("Useita työntekijöitä löytyi samalla nimellä:")
			for tyontekija in nimen_tiedot:
				for key, value in tyontekija.items():
					print(value.etunimi + " " + value.sukunimi, value.tyontekijatunnus)
			print("")
			nimi_input = input("Kumman haluat poistaa? Anna työntekijäntunnus: ")
			self.tyontekijoiden_kasitys.poista_tyontekija_tyontekijatunnuksella(nimi_input)
			print("Työntekijä poistettu")

		if len(nimen_tiedot) == 1: #Jos työntekijä löytyy, poistetaan se
			self.tyontekijoiden_kasitys.poista_tyontekija(nimi_input)
			print("Työntekijä poistettu")

		if len(nimen_tiedot) == 0: #Jos työntekijää ei löydy, tulostetaan virheilmoitus
			print("Työntekijää ei löytynyt")


	def tyontekijoiden_listaus(self): #Luodaan metodi, joka listaa työntekijät
		kaikki_tyontekijat = []
		for tyontekija_dict in tyontekijat:
			for tyontekija in tyontekija_dict.values():
				rooli = "Työntekijä" if not hasattr(tyontekija, 'alaiset') else "Esihenkilö"
				kaikki_tyontekijat.append([
					tyontekija.etunimi + " " + tyontekija.sukunimi,
					tyontekija.tyontekijatunnus,
					rooli
				])

		if not kaikki_tyontekijat:
			print("Työntekijöitä ei löytynyt")
			return
		else:
			for tyontekija in sorted(kaikki_tyontekijat, key=lambda x: (x[0], x[1])):
				print(f"Nimi: {tyontekija[0]}, Työntekijäntunnus: {tyontekija[1]}, {tyontekija[2]}")


	def tyontekijan_haku(self): #Luodaan metodi, joka hakee työntekijän
		nimi_input = input("Anna työntekijän nimi: ")
		nimen_tiedot = [ #Tarkistetaan onko samalla nimellä useampia työntekijöitä
		tyontekija_dict for tyontekija_dict in tyontekijat
		for tyontekija in tyontekija_dict.values()
		if tyontekija.etunimi + " " + tyontekija.sukunimi == nimi_input
	]

		def haun_kasittely(): #Luodaan metodi, joka käsittelee haun, optimisoidaan koodia
			for tyontekija_dict in nimen_tiedot:
				for key, value in tyontekija_dict.items():
					pattern = re.compile(r'^[A-Z]{4}\d{3}$')
					if pattern.match(nimi_input):
						tarkistus = value.tyontekijatunnus
					else:
						tarkistus = value.etunimi + " " + value.sukunimi
					if tarkistus == nimi_input:
						print("")
						print("Työntekijätunnus:", value.tyontekijatunnus)
						print("Rooli:", "Esihenkilö" if hasattr(value, 'alaiset') else "Työntekijä")
						print("Etunimi:", value.etunimi)
						print("Sukunimi:", value.sukunimi)
						print("Osasto:", value.osasto)
						print("Työnimike:", value.tyonimike)
						print("Sähköpostiosoite:", value.sahkopostiosoite)
						print("Kuukausipalkka:", value.kuukausipalkka)
						print("Työn aloitus pvm:", value.tyon_aloitus_pvm)
						if hasattr(value, 'alaiset'):
							print("Alaiset:", ', '.join([f"{alainen.etunimi} {alainen.sukunimi} - {alainen.tyontekijatunnus}" for alainen in value.alaiset]))

						input_paiva = value.tyon_aloitus_pvm if isinstance(value.tyon_aloitus_pvm, date) else datetime.strptime(value.tyon_aloitus_pvm, '%Y-%m-%d').date()
						nykypaiva = datetime.now().date()

						vuosi = nykypaiva.year - input_paiva.year
						kuukausi = nykypaiva.month - input_paiva.month
						paiva = nykypaiva.day - input_paiva.day
						if paiva < 0:
							kuukausi -= 1
							paiva += (nykypaiva.replace(day=1) - timedelta(days=1)).day
						if kuukausi < 0:
							vuosi -= 1
							kuukausi += 12

						print(f"Henkilö on ollut töissä {vuosi} vuotta, {kuukausi} kuukautta ja {paiva} päivää")

		if len(nimen_tiedot) > 1: #Jos useampia työntekijöitä löytyy, kysytään kumpaa tarkoitetaan ja tulostetaan tiedot
			print("")
			print("Useita työntekijöitä löytyi samalla nimellä:")
			for tyontekija_dict in nimen_tiedot:
				for key, value in tyontekija_dict.items():
					print(value.etunimi + " " + value.sukunimi, value.tyontekijatunnus)
			print("")
			nimi_input = input("Kumpaa tyontekijaa tarkoitat? Anna työntekijäntunnus: ")
			haun_kasittely()
		
		if len(nimen_tiedot) == 1: #Jos työntekijä löytyy, tulostetaan tiedot
			haun_kasittely()
		
		if len(nimen_tiedot) == 0: #Jos työntekijää ei löydy, tulostetaan virheilmoitus
			print("Työntekijää ei löytynyt")


	def muokkaa_tyontekija(self): #Luodaan metodi, joka muokkaa työntekijän tietoja
		tarvittava_osasto = ""
		def muokkaamisen_kasittely(): #Luodaan metodi, joka käsittelee muokkaamisen, optimisoidaan koodia
			print("Mitä haluat muuttaa?")
			print("1 Etunimi")
			print("2 Sukunimi")
			print("3 Osasto")
			print("4 Työnimike")
			print("5 Sähköpostiosoite")
			print("6 Kuukausipalkka")
			print("7 Työn aloitus pvm")
			print("8 Työntekijän alaisia")
			print("0 Peruuta")
			print("")

			komento = input("komento: ")
			if komento == "1":
				etunimi = input("Uusi etunimi: ")
				if not re.match(r'^[a-zA-ZäöåÄÖÅ]+$', etunimi):
					print("Virheellinen etunimi")
					return
				list(nimen_tiedot[0].values())[0].etunimi = etunimi
				print("Etunimi muutettu")
				return
			elif komento == "2":
				sukunimi = input("Uusi sukunimi: ")
				if not re.match(r'^[a-zA-ZäöåÄÖÅ]+$', sukunimi):
					print("Virheellinen sukunimi")
					return
				list(nimen_tiedot[0].values())[0].sukunimi = sukunimi
				print("Sukunimi muutettu")
				return
			elif komento == "3":
				osasto = input("Uusi osasto: ")
				if len(osasto) != 4:
					print("Osaston lyhenne pitää olla 4 merkkiä pitkä")
					return
				if osasto not in osasto.upper():
					print("Osaston lyhenne pitää olla isoilla kirjaimilla")
					return
				if osasto not in [osasto.split(":")[0] for osasto in osastot]:
					print("Osastoa ei ole olemassa")
					return
				for i in osastot:
					if osasto == i.split(":")[0]:
						tarvittava_osasto = i
						list(nimen_tiedot[0].values())[0].osasto = tarvittava_osasto
						if osasto not in käytetyt_id:
							käytetyt_id[osasto] = 1
						else:
							käytetyt_id[osasto] += 1
						for key, value in nimen_tiedot[0].items():
							value.tyontekijatunnus = f"{osasto}{käytetyt_id[osasto]:03d}"
						break
				print("Osasto muutettu")
				return
			elif komento == "4":
				tyonimike = input("Uusi työnimike: ")
				if not re.match(r'^[a-zA-ZäöåÄÖÅ\s]+$', tyonimike):
					print("Virheellinen työnimike")
					return
				list(nimen_tiedot[0].values())[0].tyonimike = tyonimike
				print("Työnimike muutettu")
				return
			elif komento == "5":
				sahkopostiosoite = input("Uusi sähköpostiosoite: ")
				email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
				if not re.match(email_pattern, sahkopostiosoite):
					print("Virheellinen sähköpostiosoite")
					return
				list(nimen_tiedot[0].values())[0].sahkopostiosoite = sahkopostiosoite
				print("Sähköpostiosoite muutettu")
				return
			elif komento == "6":
				kuukausipalkka = input("Uusi kuukausipalkka: ")
				if not re.match(r'^\d+(\.\d{1,2})?$', kuukausipalkka):
					print("Virheellinen kuukausipalkka")
					return
				list(nimen_tiedot[0].values())[0].kuukausipalkka = kuukausipalkka
				print("Kuukausipalkka muutettu")
				return
			elif komento == "7":
				tyon_aloitus_pvm = input("Uusi työn aloitus pvm muodossa vuosi-kuukaus-päivä: ")
				try:
					datetime.strptime(tyon_aloitus_pvm, '%Y-%m-%d')
				except ValueError:
					print("Virheellinen päivämäärä")
					return
				list(nimen_tiedot[0].values())[0].tyon_aloitus_pvm = tyon_aloitus_pvm
				print("Työn aloitus pvm muutettu")
				return
			elif komento == "8":
				if nimi_input not in [tyontekija.etunimi + " " + tyontekija.sukunimi for tyontekija_dict in tyontekijat for tyontekija in tyontekija_dict.values() if hasattr(tyontekija, 'alaiset')]:
					print("Työntekijällä ei ole alaisia")
					return
				alaiset = input("Anna alaisten työntekijäntunnukset pilkulla erotettuna: ")
				alaiset = alaiset.split(",")
				valmiit_alaiset = []
				for alainen in alaiset:
					alainen = alainen.strip()
					found = False
					for tyontekija_dict in tyontekijat:
						for tyontekija in tyontekija_dict.values():
							if alainen == tyontekija.tyontekijatunnus:
								valmiit_alaiset.append(Tyontekija(
									tyontekija.etunimi,
									tyontekija.sukunimi,
									tyontekija.osasto,
									tyontekija.tyonimike,
									tyontekija.sahkopostiosoite,
									tyontekija.kuukausipalkka,
									tyontekija.tyon_aloitus_pvm,
									tyontekija.tyontekijatunnus))
								found = True
								break
						if found:
							break
					if not found:
						print(f"Alaista {alainen} ei löydy")
						return
				list(nimen_tiedot[0].values())[0].alaiset = valmiit_alaiset
				print("")
				print("Työntekijä lisätty!")

			elif komento == "0":
				return

		nimi_input = input("Anna työntekijän nimi: ")
		nimen_tiedot = [ #Tarkistetaan onko samalla nimellä useampia työntekijöitä
		tyontekija_dict for tyontekija_dict in tyontekijat
		for tyontekija in tyontekija_dict.values()
		if tyontekija.etunimi + " " + tyontekija.sukunimi == nimi_input
	]
		if len(nimen_tiedot) > 1: #Jos useampia työntekijöitä löytyy, kysytään kumpaa tarkoitetaan ja muokataan sen tietoja
			print("Useita työntekijöitä löytyi samalla nimellä:")
			for tyontekija_dict in nimen_tiedot:
				for key, value in tyontekija_dict.items():
					print(value.etunimi + " " + value.sukunimi, value.tyontekijatunnus)
			nimi_input = input("Kumpaa tyontekijaa tarkoitat? Anna työntekijäntunnus: ")
			nimen_tiedot = [
			tyontekija_dict for tyontekija_dict in tyontekijat
			for tyontekija in tyontekija_dict.values()
			if tyontekija.tyontekijatunnus == nimi_input
		]

			muokkaamisen_kasittely()
			for tyontekija_dict in nimen_tiedot:
				for key, value in tyontekija_dict.items():
					if value.tyontekijatunnus == nimi_input:
						self.tyontekijoiden_kasitys.paivita_tyontekijat_json()
						self.tyontekijoiden_kasitys.tarkista_tyontekijatunnuksen_kopiot()
		
		elif len(nimen_tiedot) == 1: #Jos työntekijä löytyy, muokataan sen tietoja
			muokkaamisen_kasittely()
			for tyontekija_dict in tyontekijat:
				for key, value in tyontekija_dict.items():
						self.tyontekijoiden_kasitys.paivita_tyontekijat_json()
						self.tyontekijoiden_kasitys.tarkista_tyontekijatunnuksen_kopiot()

		elif len(nimen_tiedot) == 0: #Jos työntekijää ei löydy, tulostetaan virheilmoitus
			print("Ei löytynyt työntekijää")



class Sovellus: #Luodaan luokka Sovellus, joka maarittelee sovelluksen ominaisuudet
	def __init__(self): #Luodaan luokan konstruktori
		self.ohjelman_kaynnistys = OhjelmanKaynistys()
		self.osastojen_kasitys = OsastojenKasitys()
		self.osastojen_kasitys.lataa_osastot()
		self.tekninen_sovellus = TekninenSovellus()


	def ohje(self): #Luodaan metodi, joka tulostaa ohjeet
		print("")
		print("komennot:")
		print("0 lopeta")
		print("1 lisää osasto")
		print("2 osastojen listaus")
		print("3 työntekijän lisäys")
		print("4 työntekijän poistaminen")
		print("5 työntekijöiden listaus")
		print("6 työntekijähaku")
		print("7 muokkaa tyontekijan tiedot")
		print("")


	def suorita(self): #Luodaan metodi, joka suorittaa sovelluksen
		self.ohjelman_kaynnistys.lataa_tyontekijat_jsonista()
		self.ohjelman_kaynnistys.lataa_kaytetyt_id()
		while True:
			self.ohje()
			komento = input("komento: ")
			if komento == "0":
				break
			elif komento == "1":
				self.tekninen_sovellus.lisaa_osasto()
			elif komento == "2":
				self.tekninen_sovellus.osastojen_listaus()
			elif komento == "3":
				self.tekninen_sovellus.tyontekijan_lisays()
			elif komento == "4":
				self.tekninen_sovellus.tyontekijan_poisto()
			elif komento == "5":
				self.tekninen_sovellus.tyontekijoiden_listaus()
			elif komento == "6":
				self.tekninen_sovellus.tyontekijan_haku()
			elif komento == "7":
				self.tekninen_sovellus.muokkaa_tyontekija()

if __name__ == "__main__":
	Sovellus().suorita() #Käynnistetään sovellus