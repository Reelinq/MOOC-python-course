# tee ratkaisu tänne
def eniten_kirjainta(mjono):
	suurin_määrä = 0
	suurin_kirjain = " "

	for kirjain in mjono:
		määrä = mjono.count(kirjain)
		if määrä > suurin_määrä:
			suurin_määrä = määrä
			suurin_kirjain = kirjain

	return suurin_kirjain

if __name__ == '__main__':
	mjono = "abcbdbe"
	print(eniten_kirjainta(mjono))
