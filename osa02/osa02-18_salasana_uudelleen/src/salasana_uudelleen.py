# Kirjoita ratkaisu tähän
sala = input("Salasana: ")
while True:
	toisto = input("Toista salasana: ")
	if sala != toisto:
		print("Ei ollut sama!")
	else:
		break
print("Käyttäjätunnus luotu!")
