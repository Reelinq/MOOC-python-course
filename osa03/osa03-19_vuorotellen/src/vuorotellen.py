luku = int(input("Anna luku: "))
luku2 = luku
luku1 = 1
while True:
	if luku == 1:
		break
	if luku1 >= luku2:
		break	
	print(luku1)
	print(luku2)
	luku1 += 1
	luku2 -= 1
if luku %2 != 0:
	print(luku1)