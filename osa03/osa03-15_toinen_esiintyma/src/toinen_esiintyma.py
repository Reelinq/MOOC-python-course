# Kirjoita ratkaisu tähän
mjono = input("Anna merkkijono: ")
ojono = input("Anna osajono: ")
luku = 0
summa = len(ojono)

loyty = mjono.find(ojono)
if loyty >= 0:
	loyty2 = mjono.find(ojono, loyty+summa)
	if loyty2 >= 0:
		print(f"Osajonon toinen esiintymä on kohdassa {loyty2}.")
	else:
		print("Osajono ei esiinny merkkijonossa kahdesti.")
else:
	print("Osajono ei esiinny merkkijonossa kahdesti.")