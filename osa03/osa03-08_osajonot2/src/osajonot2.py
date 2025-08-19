# Kirjoita ratkaisu tähän
jono = input("Anna merkkijono: ")
kerroin = len(jono)

while True:
	kerroin -= 1
	print(jono[kerroin:])
	if kerroin == 0:
		break