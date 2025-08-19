# tee ratkaisu tänne
def uniikit(lista):
	
	uusi_lista = []
	i = 0
	luku = lista[i]
	for luku in lista:
		if luku not in uusi_lista:
			uusi_lista.append(luku)
			uusi_lista.sort()
	return uusi_lista
		


if __name__ == '__main__':
	lista = [1, 2, 2, 1, 3, 1, 3, 2, 3]
	print(uniikit(lista))