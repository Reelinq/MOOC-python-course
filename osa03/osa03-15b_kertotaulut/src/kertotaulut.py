luku = int(input("Anna luku: "))
luku1 = 1
while luku1 <= luku:
	luku2 = 1

	while luku2 <= luku:
		print(f"{luku1} x {luku2} = {luku1 * luku2}")
		luku2 += 1
	
	luku1 += 1
