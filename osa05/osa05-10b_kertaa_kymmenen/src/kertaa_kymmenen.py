def kertaa_kymmenen(alku: int, loppu: int):
	
	sanakirja = {}
	luku = alku
	while luku <= loppu:
		sanakirja[luku] = luku * 10
		luku += 1
	return sanakirja
	
if __name__ == "__main__":
	d = kertaa_kymmenen(3, 6)
	print(d)
