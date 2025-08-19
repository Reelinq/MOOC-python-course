def histogrammi(merkkijono):
	ryhmat = {}
	for kirjain in merkkijono:
		if kirjain in ryhmat:
			ryhmat[kirjain] += 1
		else:
			ryhmat[kirjain] = 1

	for kirjain, esiintymat in ryhmat.items():
		print(kirjain, "*" * esiintymat)

if __name__ == "__main__":
	histogrammi("abba")
	histogrammi("saippuakauppias")