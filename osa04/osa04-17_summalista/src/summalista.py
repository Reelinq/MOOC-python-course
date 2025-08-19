# tee ratkaisu tänne
def summa(a, b):
	uusi_lista = []
	i = 0
	while i < len(a):
		uusi_lista.append(a[i] + b[i])
		i += 1
	return uusi_lista


if __name__ == '__main__':
	a = [1, 4, 7]
	b = [7, 3, 9]
	print(summa(a, b))