def hae_sanat(hakusana: str):
	with open ("sanat.txt") as tiedosto:
		sanat = tiedosto.read().splitlines()
		tulos = []
		for sana in sanat:
			if hakusana == sana:
				tulos.append(sana)
				continue
			if "." in hakusana:
				if len(hakusana) != len(sana):
					continue
				# Käydään läpi kirjaimet
				x = True
				for i in range(len(hakusana)):
					if hakusana[i] != "." and hakusana[i] != sana[i]:
						x = False
						break
				if x:
					tulos.append(sana)
			if "*" in hakusana:
				tahti = hakusana.split("*")
				if sana.startswith(tahti[0]) and sana.endswith(tahti[1]):
					tulos.append(sana)
		return tulos