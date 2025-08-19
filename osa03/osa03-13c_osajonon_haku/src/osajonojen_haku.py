# Kirjoita ratkaisu tähän
sana = input("Sana: ")
merkki = input("Merkki: ")
merkit = sana.find(merkki)
merkki1 = merkit + 1
merkki2 = merkit + 3
if merkit == len(sana):
	print()

if merkit + 1 == len(sana) -1:
	print()

elif merkki in sana:
	print(sana[merkit:merkki2])