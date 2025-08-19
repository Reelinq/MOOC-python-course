import csv, datetime
def huijarit():
	with open ("tentin_aloitus.csv") as t, open ("palautus.csv") as t2:
		list = []
		list2 = []
		for i in csv.reader(t, delimiter=";"):
			list.append(i)
		for i in csv.reader(t2, delimiter=";"):
			list2.append(i)

		valmis = []
		for i in list:
			for j in list2:
				if i[0] == j[0]:
					suurempi = datetime.datetime.strptime(j[-1], "%H:%M")
					pienempi = datetime.datetime.strptime(i[-1], "%H:%M")
					if suurempi - pienempi > datetime.timedelta(hours=3):
						valmis.append(i[0])

		for i in valmis:
			if valmis.count(i) > 1:
				valmis.remove(i)

	return valmis

if __name__ == "__main__":
	print(huijarit())