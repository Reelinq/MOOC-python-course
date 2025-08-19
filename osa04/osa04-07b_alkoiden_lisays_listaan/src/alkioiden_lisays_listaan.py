# Kirjoita ratkaisu tähän
monta = int(input("Kuinka monta lukua?"))
list = []
i = 1
while i <= monta:
	luku = int(input(f"Anna {i} luku"))
	list.append(luku)
	i += 1
print(list)