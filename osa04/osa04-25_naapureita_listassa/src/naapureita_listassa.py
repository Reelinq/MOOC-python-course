# tee ratkaisu tänne
def pisin_naapurijono(lista):
	pisin = 0
	pisin2 = 0
	for luku in range(len(lista)-1):
		if lista[luku+1] == lista[luku]+1 or lista[luku+1] == lista[luku]-1:
			pisin += 1
		else:
			if pisin > pisin2:
				pisin2 = pisin
			pisin = 0

	if pisin > pisin2:
		pisin2 = pisin
	
	return pisin2 + 1

if __name__ == '__main__':
	lista = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
	print(pisin_naapurijono(lista))
