from random import randint
from string import ascii_lowercase
def luo_salasana(pituus):
	salasana = ""
	for i in range(pituus):
		salasana += ascii_lowercase[randint(0, len(ascii_lowercase)) -1]
	return salasana