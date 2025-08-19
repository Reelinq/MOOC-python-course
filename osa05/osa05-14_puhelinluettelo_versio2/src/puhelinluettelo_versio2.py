# tee ratkaisu tänne
nimet = {}
while True:
	luku = int(input("Komento (1 hae, 2 lisää, 3 lopeta): "))

	if luku == 1:
		nimenhaku = input("nimi: ")
		if nimenhaku in nimet:
			print(nimet[nimenhaku])
		else:
			print("ei numeroa")

	if luku == 2:
		nimi = input("nimi: ")
		numero = input("numero: ")
		if nimi in nimet:
			nimet[nimi] += "\n" + numero
			print("ok!")
		else:
			print("ok!")
			nimet[nimi] = numero

	if luku == 3:
		print("lopetetaan...")
		break
