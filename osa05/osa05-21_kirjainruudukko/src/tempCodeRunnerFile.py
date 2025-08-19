kerrokset = int(input("Kerrokset: "))
aakkoset = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
aakkoset_uusi = []
list = [[]]

for i in range(kerrokset):
	aakkoset_uusi.append(aakkoset[i])

for i in aakkoset_uusi:
	if i == "a":
		list[0].append(aakkoset_uusi[0])
	list[0].insert(0, i)
	list[0].insert(-1, i)

	print(list)