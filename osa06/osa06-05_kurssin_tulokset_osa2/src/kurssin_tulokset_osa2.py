opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")
koepisteet = input("Koepisteet: ")

ot = {}

with open ("./src/opiskelijat1.csv") as tiedosto:
	for i in tiedosto:
		j = i.replace("\n", "").split(";")
		if j[0] == "opnro":
			continue
		ot[j[0]] = j[1], j[2]

tt = {}

with open ("./src/tehtavat1.csv") as tiedosto:
	for i in tiedosto:
		j = i.replace("\n", "").split(";")
		if j[0] == "opnro":
			continue
		tt[j[0]] = min(sum(map(int, j[1:])), 40)// 4

kp = {}

with open ("./src/koepisteet1.csv") as tiedosto:
	for i in tiedosto:
		j = i.replace("\n", "").split(";")
		if j[0] == "opnro":
			continue
		kp[j[0]] = sum(map(int, j[1:]))

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
	print(nimi[0], nimi[1], arvosana)	