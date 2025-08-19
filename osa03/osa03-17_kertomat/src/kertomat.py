# Kirjoita ratkaisu tähän
while True:
	luku = int(input("Anna luku: "))
	kerroin = 1
	kerroin2 = 1
	while True:
		kerroin = kerroin * kerroin2
		kerroin2 += 1
		if kerroin2 > luku:
			break
	if luku <= 0:
		print("Kiitos ja moi!")
		break
	print(f"Luvun {luku} kertoma on {kerroin}")

