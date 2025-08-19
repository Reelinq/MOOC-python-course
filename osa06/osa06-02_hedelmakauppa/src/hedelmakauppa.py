def lue_hedelmat():
	with open ("./src/hedelmat.csv") as tiedosto:
		sanakirja = {}
		for i in tiedosto:
			luku = i.replace("\n", "")
			sanat = luku.split(";")
			sanakirja[sanat[0]] = float(sanat[1])
	return sanakirja