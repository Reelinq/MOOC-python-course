def kertomat(n: int):
	kertomakirja = {}
	kertoma = 1
	for i in range(1, n + 1):
		kertoma *= i
		kertomakirja[i] = kertoma
	return(kertomakirja)

if __name__ == "__main__":
	k = kertomat(5)
	print(k[1])
	print(k[3])
	print(k[5])
