# tee ratkaisu tänne
def vanhemmat(henkilot: list, vuosi: int):
	lista = []
	for i in henkilot:
		if i[1] < vuosi:
			lista.append(i[0])
	return lista

if __name__ == "__main__":
	h1 = ("Arto", 1977)
	h2 = ("Einari", 1985)
	h3 = ("Maija", 1953)
	h4 = ("Essi", 1997)
	hlista = [h1, h2, h3, h4]

	vanhemmat_henkilot = vanhemmat(hlista, 1979)
	print(vanhemmat_henkilot)
