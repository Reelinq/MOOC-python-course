# tee ratkaisu tänne
def pisimman_pituus(lista):
	paras = "ju"
	for alkio in lista:
		if len(alkio) > len(paras):
			paras = alkio
	
	i = len(paras)
	return i
        
if __name__ == "__main__":
	lista = ["eka", "toka", "kolmas", "seitsemäs"]
	tulos = pisimman_pituus(lista)
	print(tulos)