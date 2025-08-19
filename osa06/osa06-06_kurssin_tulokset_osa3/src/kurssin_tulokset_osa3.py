opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")
koepisteet = input("Koepisteet: ")

ot = {}

with open (opiskelijatiedot) as tiedosto:
	for i in tiedosto:
		j = i.replace("\n", "").split(";")
		if j[0] == "opnro":
			continue
		ot[j[0]] = j[1], j[2]

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

with open (koepisteet) as tiedosto:
	for i in tiedosto:
		j = i.replace("\n", "").split(";")
		if j[0] == "opnro":
			continue
		kp[j[0]] = sum(map(int, j[1:]))

print("{:29} {:9} {:9} {:9} {:9} {:9}".format("nimi", "teht_lkm", "teht_pist", "koe_pist", "yht_pist", "arvosana"))

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
	print("{:29} {:<9} {:<9} {:<9} {:<9} {:<9}".format(kokonimi, tehtlkm[x], tt[opnro], kp[opnro], yht, arvosana))
	x += 1