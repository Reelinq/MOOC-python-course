# tee ratkaisu tänne
def positiivisten_summa(lista):
	summa = 0
	for i in lista:
		if i > 0:
			summa += i
	return summa

if __name__ == "__main__":
	print(positiivisten_summa([1, -2, 3, -4, 5]))