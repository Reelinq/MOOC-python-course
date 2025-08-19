from random import randint, sample
from string import ascii_lowercase, digits
def luo_hyva_salasana(pituus, numero, erikoismerkki):
	merkit = list(ascii_lowercase)
	salasana = list(ascii_lowercase)[randint(0, len(ascii_lowercase)) -1]
	if numero:
		merkit += list(digits)
		salasana += list(digits)[randint(0, len(digits)) -1]
	if erikoismerkki:
		merkit += list("!?=+-()#")
		salasana += list("!?=+-()#")[randint(0, len("!?=+-()#")) -1]
	while len(salasana) < pituus:
		salasana += merkit[randint(0, len(merkit)) -1]
	return "".join(sample(salasana, len(salasana)))