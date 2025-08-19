def suodata_virheelliset():
	with open ("lottonumerot.csv") as tiedosto, open("korjatut_numerot.csv", "w") as korjattu:
		for rivi in tiedosto:
			lotot = rivi.split(";")
			viikko = lotot[0].split(" ")
			numerot = lotot[1].strip().split(",")

			if viikko[1] not in [str(x) for x in range(1, 53)]:
				continue

			x = True
			for i in numerot:
				if i in [str(x) for x in range(1, 39)]:
					continue
				x = False
				break
			if x == False:
				continue

			if len(numerot) != 7:
				continue

			if len(set(numerot)) != 7:
				continue

			korjattu.write(rivi)