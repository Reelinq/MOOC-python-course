# Kirjoita ratkaisu tähän
asti = int(input("Mihin asti: "))
kerroin = int(input("Mikä kerroin: "))
luku = 1

while luku <= asti:
	print(luku)
	luku *= kerroin
	if luku > asti + 1:
		luku = asti + 2
