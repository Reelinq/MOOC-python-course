# Kirjoita ratkaisu tähän
list = []
while True:
	sana = input("Sana: ")
	if sana in list:
		break
	list.append(sana)
print(f"Annoit {len(list)} eri sanaa")
