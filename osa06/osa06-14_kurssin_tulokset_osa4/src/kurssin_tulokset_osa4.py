opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")
koepisteet = input("Koepisteet: ")
kurssin_tiedot = input("Kurssin tiedot: ")

with open ("tulos.txt", "w") as tulos, open ("tulos.csv", "w") as tulos2:

	nl_list = []
	with open (kurssin_tiedot) as tiedosto:
		for i in tiedosto:
			nl_list.append(i.split(":")[1].strip())
	x = nl_list[0] + ", " + nl_list[1] + " opintopistettä"
	tulos.write(x + "\n")
	tulos.write("=" * len(x) + "\n")

	ot = {}
	f_opnro = []

	with open (opiskelijatiedot) as tiedosto:
		for i in tiedosto:
			j = i.replace("\n", "").split(";")
			if j[0] == "opnro":
				continue
			ot[j[0]] = j[1], j[2]
			f_opnro.append(j[0])

	tt = {}
	tehtlkm = []
	x = 0

	with open (tehtavatiedot) as tiedosto:
		for i in tiedosto:
			j = i.replace("\n", "").split(";")
			if j[0] == "opnro":
				continue
			tehtlkm.append(sum(map(int, j[1:])))
			tt[j[0]] = min(sum(map(int, j[1:])), 40)// 4
			

	kp = {}
	f_nimi = []
	arv = []

	with open (koepisteet) as tiedosto:
		for i in tiedosto:
			j = i.replace("\n", "").split(";")
			if j[0] == "opnro":
				continue
			kp[j[0]] = sum(map(int, j[1:]))

	tulos.write("{:29} {:9} {:9} {:9} {:9} {:9}".format("nimi", "teht_lkm", "teht_pist", "koe_pist", "yht_pist", "arvosana") + "\n")

	for opnro, nimi in ot.items():
		yht = tt[opnro] + kp[opnro]
		if yht <= 14:
			arvosana = 0
		elif yht <= 17:
			arvosana = 1
		elif yht <= 20:
			arvosana = 2
		elif yht <= 23:
			arvosana = 3
		elif yht <= 27:
			arvosana = 4
		else:
			arvosana = 5
		kokonimi = nimi[0] + " " + nimi[1]
		f_nimi.append(kokonimi)
		arv.append(str(arvosana))
		tulos.write("{:29} {:<9} {:<9} {:<9} {:<9} {:<9}".format(kokonimi, tehtlkm[x], tt[opnro], kp[opnro], yht, arvosana) + "\n")
		x += 1

	y = ""
	for i in range(len(f_opnro)):
		y += f_opnro[i] + ";" + f_nimi[i] + ";" + arv[i] + "\n"
	tulos2.write(y)