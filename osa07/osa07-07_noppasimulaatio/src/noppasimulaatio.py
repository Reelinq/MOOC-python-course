from random import randint
def heita(noppa: str):
	noppa_a = 3, 3, 3, 3, 3, 6
	noppa_b = 2, 2, 2, 5, 5, 5
	noppa_c = 1, 4, 4, 4, 4, 4
	if noppa == "A":
		return noppa_a[randint(0, 5)]
	elif noppa == "B":
		return noppa_b[randint(0, 5)]
	elif noppa == "C":
		return noppa_c[randint(0, 5)]

def pelaa(noppa1: str, noppa2: str, kertaa: int):
	voitot1 = 0
	voitot2 = 0
	tasapelit = 0
	for i in range(kertaa):
		tulos1 = heita(noppa1)
		tulos2 = heita(noppa2)
		if tulos1 > tulos2:
			voitot1 += 1
		elif tulos1 < tulos2:
			voitot2 += 1
		else:
			tasapelit += 1
	return voitot1, voitot2, tasapelit