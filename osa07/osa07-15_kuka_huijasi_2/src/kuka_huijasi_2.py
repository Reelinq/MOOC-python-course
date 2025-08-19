import csv, datetime
def viralliset_pisteet():
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
					if suurempi - pienempi < datetime.timedelta(hours=3):
						valmis.append(j)

		sk = {}
		kk = {}
		for i in valmis:
			if i[0] not in kk:
				kk[i[0]] = {}
			if kk[i[0]].get(i[1], 0) < int(i[2]):
				kk[i[0]][i[1]] = int(i[2])

			for i in kk:
				sk[i] = sum(kk[i].values())

	return sk

if __name__ == "__main__":
	print(viralliset_pisteet())