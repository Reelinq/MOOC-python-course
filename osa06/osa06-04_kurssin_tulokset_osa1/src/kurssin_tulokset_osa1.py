opiskelijatiedot = input("Opiskelijatiedot: ")
ot = {}

with open (opiskelijatiedot) as tiedosto:
	for i in tiedosto:
		j = i.replace("\n", "").split(";")
		if j[0] == "opnro":
			continue
		ot[j[0]] = j[1], j[2]

tehtävätiedot = input("Tehtävätiedot: ")
tt = {}

with open (tehtävätiedot) as tiedosto:
	for i in tiedosto:
		j = i.replace("\n", "").split(";")
		if j[0] == "opnro":
			continue
		tt[j[0]] = sum(map(int, j[1:]))

for opnro, nimi in ot.items():
	arvosana = tt[opnro]
	print(nimi[0], nimi[1], arvosana)