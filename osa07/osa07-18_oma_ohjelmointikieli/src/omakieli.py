def suorita(lista):
	output = []
	muuttujat = {}
	idx = 0
	idx2 = 0
	
	for i in lista:
		i = i.split()
		kom = i[0]
		if kom[-1] == ":":
			muuttujat[kom] = idx2
		idx2 += 1

	while idx < len(lista):
		komento = lista[idx].split()
		kom = komento[0]

		if kom == "END":
			break
		elif kom == "PRINT":
			if komento[1].isdigit():
				output.append(int(komento[1]))
			else:
				output.append(muuttujat.get(komento[1], 0))
		elif kom == "MOV":
			if komento[2].isdigit():
				muuttujat[komento[1]] = int(komento[2])
			else:
				muuttujat[komento[1]] = muuttujat.get(komento[2], 0)
		elif kom == "ADD":
			if komento[1] not in muuttujat:
				muuttujat[komento[1]] = 0
			if komento[2].isdigit():
				muuttujat[komento[1]] = muuttujat.get(komento[1]) + int(komento[2])
			else:
				muuttujat[komento[1]] = muuttujat.get(komento[1]) + muuttujat.get(komento[2])
		elif kom == "SUB":
			if komento[2].isdigit():
				muuttujat[komento[1]] = muuttujat.get(komento[1]) - int(komento[2])
			else:
				muuttujat[komento[1]] = muuttujat.get(komento[1]) - muuttujat.get(komento[2])
		elif kom == "MUL":
			if komento[2].isdigit():
				muuttujat[komento[1]] = muuttujat.get(komento[1]) * int(komento[2])
			else:
				muuttujat[komento[1]] = muuttujat.get(komento[1]) * muuttujat.get(komento[2])
		elif kom == "JUMP":
			idx = muuttujat.get(komento[1] + ":")
		elif kom == "IF":
			if komento[3].isdigit():
				value1 = muuttujat.get(komento[1])
				value2 = int(komento[3])
			else:
				value1 = muuttujat.get(komento[1])
				value2 = muuttujat.get(komento[3])
			if komento[2] == ">" and value1 > value2:
				idx = muuttujat.get(komento[5] + ":")
			elif komento[2] == ">=" and value1 >= value2:
				idx = muuttujat.get(komento[5] + ":")
			elif komento[2] == "<" and value1 < value2:
				idx = muuttujat.get(komento[5] + ":")
			elif komento[2] == "<=" and value1 <= value2:
				idx = muuttujat.get(komento[5] + ":")
			elif komento[2] == "==" and value1 == value2:
				idx = muuttujat.get(komento[5] + ":")
			elif komento[2] == "!=" and value1 != value2:
				idx = muuttujat.get(komento[5] + ":")
		idx += 1

	return output

if __name__ == '__main__':
	ohjelma4 = ['MOV A 1', 'MOV B 1', 'alku:', 'MUL A 2', 'ADD B 1', 'IF B != 101 JUMP alku', 'PRINT A']
	tulos = suorita(ohjelma4)
	print(tulos)