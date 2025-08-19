# Kirjoita ratkaisu tähän
jono = input("Anna merkkijono: ")
kerroin = 0

while True:
	kerroin += 1
	print(jono[:kerroin])
	if kerroin == len(jono):
		break