# Tee ratkaisu tänne
def anagrammi(sana1, sana2):
	sana1 = sorted(sana1)
	sana2 = sorted(sana2)
	return sana1 == sana2

if __name__ == "__main__":
	anagrammi = ("talo", "olat")