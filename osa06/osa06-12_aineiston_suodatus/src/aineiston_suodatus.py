def suodata_laskut():
	with open ("oikeat.csv", "w") as oikeat, open ("vaarat.csv", "w") as vaarat, open ("laskut.csv") as laskut:
		o = ""
		v = ""
		for i in laskut:
			j = i.strip().split(";")
			if "+" in j[1]:
				x = j[1].split("+")
				tulos = int(x[0]) + int(x[1])
			elif "-" in j[1]:
				x = j[1].split("-")
				tulos = int(x[0]) - int(x[1])
			if tulos == int(j[2]):
				o += i
			else:
				v += i
		oikeat.write(o)
		vaarat.write(v)