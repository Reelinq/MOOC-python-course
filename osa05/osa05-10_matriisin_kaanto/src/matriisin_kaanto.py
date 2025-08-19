# tee ratkaisu tänne
def transponoi(matriisi):
    n = len(matriisi)
    for i in range(n):
        for j in range(i, n):
            matriisi[i][j], matriisi[j][i] = matriisi[j][i], matriisi[i][j]

if __name__ == '__main__':
	matriisi = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	print(transponoi(matriisi))
