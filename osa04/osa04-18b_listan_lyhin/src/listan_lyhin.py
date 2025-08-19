# tee ratkaisu tänne
def lyhin(lista):
	paras = "junsjoiewqjpkdsvijfewöldsflkmdsokwäpsankmewqölnnoirewpqkjlfkrenwmökjgrpewåklf"
	for alkio in lista:
		if len(alkio) < len(paras):
			paras = alkio
	return paras


if __name__ == "__main__":
	lista = ["eka", "toka", "kolmas", "seitsemäs"]
	tulos = lyhin(lista)
	print(tulos)
