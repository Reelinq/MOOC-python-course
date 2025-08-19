# Kirjoita ratkaisu tähän
asti = int(input("Mihin asti: "))
luku = 1

while luku <= asti:
	print(luku)
	luku *= 2
	if luku > asti + 1:
		luku = asti + 2
