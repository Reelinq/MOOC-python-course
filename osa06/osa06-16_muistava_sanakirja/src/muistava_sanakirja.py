while True:
	print("1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu")
	valinta = int(input("Valinta: "))

	if valinta == 1:
		sanas = input("Anna sana suomeksi: ")
		sanae = input("Anna sana englanniksi: ")
		with open ("sanakirja.txt", "a") as tiedosto:
			tiedosto.write(sanas + "." + sanae + "\n")
		print("Sanapari lisätty")

	if valinta == 2:
		sana = input("Anna sana: ")
		with open ("sanakirja.txt") as tiedosto:
			for i in tiedosto:
				j = i.strip().split(".")
				if sana in j[0] or sana in j[1]:
					print(j[0] + " - " + j[1])

	if valinta == 3:
		print("Moi!")
		break