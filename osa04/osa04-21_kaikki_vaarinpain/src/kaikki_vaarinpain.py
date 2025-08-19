# tee ratkaisu tänne
def kaikki_vaarinpain(lista):
	uusi_lista = []
	i = 0
	while i < len(lista):
		uusi_lista.append(lista[i][::-1])
		i += 1


	uusi_lista2 = uusi_lista[::-1]
	return uusi_lista2


if __name__ == '__main__':
	lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
	lista2 = kaikki_vaarinpain(lista)
	print(lista2)