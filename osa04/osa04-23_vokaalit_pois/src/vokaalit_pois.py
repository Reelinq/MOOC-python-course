# tee ratkaisu tänne
def ilman_vokaaleja(mjono):
	vokaalit = ["a", "e", "i", "o", "u", "y", "å", "ä", "ö"]
	uusi_mjono = ""
	for kirjain in mjono:
		if kirjain not in vokaalit:
			uusi_mjono += kirjain
	return uusi_mjono


if __name__ == '__main__':
	mjono = "tämä on esimerkki"
	print(ilman_vokaaleja(mjono))
