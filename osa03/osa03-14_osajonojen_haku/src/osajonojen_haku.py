# Kirjoita ratkaisu tähän
sana = input("Sana: ")
merkki = input("Merkki: ")
luku = 0

while luku < len(sana)-2:
	if sana[luku] == merkki:
		print(sana[luku:luku+3])
	luku += 1



