# Kirjoita ratkaisu tähän
while True:
	editori = input("Editori: ")

	if editori.lower() == "word" or editori.lower() == "notepad":
		print("surkea")
	elif editori.lower() == "visual studio code":
		print("loistava valinta!")
		break
	else:
		print("ei ole hyvä")