from random import sample
def sanat(n: int, alku: str):
	with open ("sanat.txt") as tiedosto:
		list = []
		for i in tiedosto:
			if i.startswith(alku):
				list.append(i)
		return sample(list, n)