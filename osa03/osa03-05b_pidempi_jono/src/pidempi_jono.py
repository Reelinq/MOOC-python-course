# Kirjoita ratkaisu tähän
jono1 = (input("Anna jono 1:"))
jono2 = (input("Anna jono 2:"))

if (len(jono1)) > (len(jono2)):
				  print(f"{jono1} on pidempi")

elif (len(jono2)) > (len(jono1)):
					print(f"{jono2} on pidempi")

else:
	print("Jonot ovat yhtä pitkät")