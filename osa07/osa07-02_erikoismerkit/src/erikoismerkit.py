from string import ascii_letters, punctuation
def jaa_merkkeihin(merkkijono: str):
	jono1 = ""
	jono2 = ""
	jono3 = ""
	for i in merkkijono:
		if i in ascii_letters:
			jono1 += i
		elif i in punctuation:
			jono2 += i
		else:
			jono3 += i
	return(jono1, jono2, jono3)