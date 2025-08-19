# TEE RATKAISUSI TÄHÄN:
import re

def on_viikonpaiva(merkkijono: str):
	if re.search("^(ma|ti|ke|to|pe|la|su)$", merkkijono):
		return True
	else:
		return False

def kaikki_vokaaleja(merkkijono: str):
	return len(re.findall("[aeiouyåöäAEIOUYÅÖÄ]", merkkijono)) == len(merkkijono)

def kellonaika(merkkijono: str):
	if re.search("^([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$", merkkijono):
		return True
	else:
		return False