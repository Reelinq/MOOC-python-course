from difflib import get_close_matches
lause = input("write text:")

sanatvaarin = []
uusilause = ""

with open ("wordlist.txt") as t:
	sanat = t.read().splitlines()
	for sana in lause.split():
		if sana.lower() in sanat:
			uusilause += sana + " "
		else:
			sanatvaarin.append(sana)
			uusilause += "*" + sana + "* "

	
	for vaarasana in sanatvaarin:
		print(uusilause)
		print(vaarasana + ": " + ", ".join(get_close_matches(vaarasana, sanat)))