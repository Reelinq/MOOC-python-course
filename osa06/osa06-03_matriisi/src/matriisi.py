def summa():
	with open ("./src/matriisi.txt") as tiedosto:
		summa = 0
		for i in tiedosto:
			for j in i.replace("\n", "").split(","):
				summa += int(j)
		return summa
	
def maksimi():
	with open ("./src/matriisi.txt") as tiedosto:
		maksimi = float("-inf")
		for i in tiedosto:
			for j in i.replace("\n", "").split(","):
				if maksimi < int(j):
					maksimi = int(j)
		return maksimi

def rivisummat():
	with open ("./src/matriisi.txt") as tiedosto:
		summat = []
		for i in tiedosto:
			summa = 0
			for j in i.replace("\n", "").split(","):
				summa += int(j)
			summat.append(summa)
		return summat