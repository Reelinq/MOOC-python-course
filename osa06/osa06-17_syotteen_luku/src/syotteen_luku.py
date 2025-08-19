def lue(luku, min, max):
	while True:
		try:
			arvo = int(input(luku))
			if arvo >= min and arvo <= max:
				return arvo
		except ValueError:
			pass
		print("Syötteen on oltava kokonaisluku väliltä " + str(min) + "..." + str(max))