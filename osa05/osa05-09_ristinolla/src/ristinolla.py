# tee ratkaisu tänne
def pelaa_siirto(lauta: list, x: int, y: int, nappula: str):
	if x >= 3 or x <= -1 or y >= 3 or y <= -1:
		return False
	if lauta[y][x] == "":
		lauta[y][x] = nappula
		return True
	else:
		return False
	









if __name__ == '__main__':
	lauta = [["", "", ""], ["", "", ""], ["", "", ""]]
	print(pelaa_siirto(lauta, 2, 0, "X"))
	print(lauta)