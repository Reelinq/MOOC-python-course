from datetime import datetime
def onko_validi(hetu: str):
	if len(hetu) != 11:
		return False
	
	paiva = hetu[:2]
	kuukausi = hetu[2:4]
	vuosi = hetu[4:6]
	valimerkki = hetu[6]
	yksilonumero = hetu[7:10]
	tarkistusmerkki = hetu[-1]

	if valimerkki == "+":
		vuosialku = "18"
	elif valimerkki == "-":
		vuosialku = "19"
	elif valimerkki == "A":
		vuosialku = "20"
	else:
		return False

	try:
		syntyma = datetime(int(vuosialku + vuosi),int(kuukausi),int(paiva))
	except ValueError:
		return False
	
	tarkistus = paiva + kuukausi + vuosi + yksilonumero
	tarkistus = int(tarkistus) % 31
	x = 0
	for i in "0123456789ABCDEFHJKLMNPRSTUVWXY":
		x += 1
		if tarkistusmerkki == i:
			if tarkistus == x - 1:
				return True
			else:
				return False