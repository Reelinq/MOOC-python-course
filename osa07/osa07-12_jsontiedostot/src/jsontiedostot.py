import json
def tulosta_henkilot(tiedosto: str):
	with open(tiedosto, "r") as t:
		data = json.loads(t.read())
		for i in data:
			nimi = i["nimi"]
			ika = i["ika"]
			harrastukset = i["harrastukset"]
			harrastukset_str = ", ".join(harrastukset)
			print(f"{nimi} {ika} vuotta ({harrastukset_str})")