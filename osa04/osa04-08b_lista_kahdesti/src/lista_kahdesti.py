# Kirjoita ratkaisu tähän
list = []
while True:
	luku = int(input("Anna luku: "))
	if luku == 0:
		break
	list.append(luku)
	print(f"Lista: {list}")
	print(f"Järjestettynä: {sorted(list)}")
print("Moi!")