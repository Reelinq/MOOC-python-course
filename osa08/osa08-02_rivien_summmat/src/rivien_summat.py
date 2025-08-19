def rivien_summat(matriisi: list):
	summa = 0
	for i in range(len(matriisi)):
		for j in matriisi[i]:
			summa += j
		matriisi[i].append(summa)
		summa = 0
