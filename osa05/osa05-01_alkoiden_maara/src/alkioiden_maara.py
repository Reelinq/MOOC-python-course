# tee ratkaisu tänne
def laske_alkiot(matriisi: list, alkio: int):
	summa = 0
	for i in range(len(matriisi)):
		for x in range(len(matriisi[i])):
			if alkio == matriisi[i][x]:
				summa += 1
	return summa

if __name__ == "__main__":
	m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
	print(laske_alkiot(m, 1))
