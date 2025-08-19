# tee ratkaisu tänne
def parilliset(lista):
	uusi_lista = []

	for i in lista:
		if i % 2 == 0:
			uusi_lista.append(i)
	return uusi_lista



if __name__ == '__main__':
	lista = [1,2,3,4,5]
	uusi_lista = parilliset(lista)
	print(lista)
	print(uusi_lista)