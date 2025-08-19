def parilliset(alku: int, maksimi: int):
	luku = alku
	while luku <= maksimi:
		if luku % 2 == 0:
			yield luku
		luku += 1