def lukukirja():
	numerot = {
	    0: "nolla", 1: "yksi", 2: "kaksi", 3: "kolme", 4: "neljä", 5: "viisi",
	    6: "kuusi", 7: "seitsemän", 8: "kahdeksan", 9: "yhdeksän", 10: "kymmenen",
	    11: "yksitoista", 12: "kaksitoista", 13: "kolmetoista", 14: "neljätoista",
	    15: "viisitoista", 16: "kuusitoista", 17: "seitsemäntoista", 18: "kahdeksantoista",
	    19: "yhdeksäntoista", 20: "kaksikymmentä", 30: "kolmekymmentä", 40: "neljäkymmentä",
	    50: "viisikymmentä", 60: "kuusikymmentä", 70: "seitsemänkymmentä", 80: "kahdeksankymmentä",
	    90: "yhdeksänkymmentä"
	}

	luvut = {}
	for i in range(100):
		if i in numerot:
			luvut[i] = numerot[i]
		else:
			kymmenet = i // 10 * 10
			ykköset = i % 10
			luvut[i] = numerot[kymmenet] + numerot[ykköset]

	return luvut


if __name__ == "__main__":
	luvut = lukukirja()
	print(luvut[2])
	print(luvut[11])
	print(luvut[45])
	print(luvut[99])
	print(luvut[0])
