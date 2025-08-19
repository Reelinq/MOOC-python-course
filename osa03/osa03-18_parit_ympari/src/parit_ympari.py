# Kirjoita ratkaisu tähän
luku = int(input("Anna luku: "))
kerroin = 2
while True:
	kerroin1 = kerroin - 1
	if kerroin - 1 == luku:
		print(kerroin - 1)
	else:
		print(kerroin)
	if kerroin > luku:
		break
	print(kerroin1)
	kerroin += 2
	if kerroin1 >= luku:
		break
	if kerroin > luku:
		break
if luku %2 != 0 and luku != 1:
	print(luku)