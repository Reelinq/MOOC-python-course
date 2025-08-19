# tee ratkaisu tänne
def kumpi_voitti(pelilauta: list):
	pelaaja1 = []
	pelaaja2 = []
	for i in pelilauta:
		for j in i:
			if 1 == j:
				pelaaja1.append(1)
			elif 2 == j:
				pelaaja2.append(1)
	if len(pelaaja1) > len(pelaaja2):
		return 1
	elif len(pelaaja1) < len(pelaaja2):
		return 2
	else:
		return 0

if __name__ == '__main__':
	list = [[2, 1, 0, 2], [1, 1, 1, 2,], [2, 0, 0, 1,], [1, 1, 1, 1]]
	print(kumpi_voitti(list))