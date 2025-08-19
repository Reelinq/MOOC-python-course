# Kirjoita ratkaisu tähän
jono = input("Anna lause: ")
print(jono[0])
loyda = 0
while True:
	loyda = jono.find(" ", loyda+1)
	if loyda == -1:
		break
	print(jono[loyda+1])
	