import datetime

def vuodet_listaan(paivamaarat: list):
	lista = []
	for i in paivamaarat:
		lista.append(i.year)
	if len(lista) > 1:
		lista.sort()
	return lista