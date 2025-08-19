# tee ratkaisu tänne
def palindromi(sana):
	return sana == sana[::-1]
while True:
	p = input("Anna palindromi: ")
	if palindromi(p):
		print(f"{p} on palindromi!")
		break
	else:
		print("ei ollut palindromi")
# huomaa, että tällä kertaa pääohjelmaa ei tule kirjoittaa lohkon
# if __name__ == "__main__":
# sisälle!
