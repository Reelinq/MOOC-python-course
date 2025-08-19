# tee ratkaisu tänne
def poista_isot(lista):
	uusi_lista = []

	for sana in lista:
		if not sana.isupper():
			uusi_lista.append(sana)
	return uusi_lista

if __name__ == '__main__':
	lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
	karsittu_lista = poista_isot(lista)
	print(karsittu_lista)
