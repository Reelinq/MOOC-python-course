# tee ratkaisu tänne
def pisimmat(lista):
	uusi_lista = []
	paras = 0
	for alkio in lista:
		if len(alkio) > paras:
			paras = len(alkio)
	for alkio in lista:
		if len(alkio) == paras:
			uusi_lista.append(alkio)
	return uusi_lista

if __name__ == "__main__":
	lista = ["eka", "toka", "kolmas", "seitsemäs"]
	tulos = pisimmat(lista)
	print(tulos)
