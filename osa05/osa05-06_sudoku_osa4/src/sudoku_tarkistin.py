# tee ratkaisu tänne
def rivi_oikein(sudoku: list[list[int]]):
	for i in sudoku:
		lista = []
		for j in i:
			if j in lista:
				return False
			if j > 0:
				lista.append(i)
	return True


def sarake_oikein(sudoku: list[list[int]]):
	for j in range(9):
		lista = []
		for i in sudoku:
			if i[j] in lista:
				return False
			if i[j] > 0:
				lista.append(i[j])
	return True


def nelio_oikein(sudoku: list[list[int]]):
	lista: list[list[int]] = [[], [], [], [], [], [], [], [], []]
	for i in range(9):
		for j in range(9):
			numero = sudoku[i][j]
			if numero == 0:
				continue
			list = lista[i // 3 + j // 3 * 3]
			if numero in list:
				return False
			if numero > 0:
				list.append(numero)
	return True


def sudoku_oikein(sudoku: list[list[int]]):
	if rivi_oikein(sudoku) and sarake_oikein(sudoku) and nelio_oikein(sudoku) == True:
		return True
	else:
		return False


if __name__ == '__main__':
	sudoku1 = [
		[9, 0, 0, 0, 8, 0, 3, 0, 0],
		[2, 0, 0, 2, 5, 0, 7, 0, 0],
		[0, 2, 0, 3, 0, 0, 0, 0, 4],
		[2, 9, 4, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 7, 3, 0, 5, 6, 0],
		[7, 0, 5, 0, 6, 0, 4, 0, 0],
		[0, 0, 7, 8, 0, 3, 9, 0, 0],
		[0, 0, 1, 0, 0, 0, 0, 0, 3],
		[3, 0, 0, 0, 0, 0, 0, 0, 2]
	]

	print(sudoku_oikein(sudoku1))

	sudoku2 = [
	[ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
	[ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
	[ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
	[ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
	[ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
	[ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
	[ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
	[ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
	[ 3, 0, 1, 5, 0, 6, 4, 9, 0 ],
	]

	print(sudoku_oikein(sudoku2))
