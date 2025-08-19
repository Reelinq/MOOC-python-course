teksti = []

with open ("wordlist.txt") as tiedosto:
	for i in tiedosto:
		j = i.replace("\n", "")
		teksti.append(j)

txt = input("Write text: ")
uusi_input = txt.split(" ")

for i in range(len(uusi_input)):
	if uusi_input[i].lower() not in teksti:
		uusi_input[i] = "*" + uusi_input[i] + "*"

print(" ".join(uusi_input))
