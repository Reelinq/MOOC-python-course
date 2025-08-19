luvut = ""
kierros = 0
summa = 0
positiivinen = 0
negatiivinen = 0
print("Syötä kokonaislukuja, 0 lopettaa:")
while True:
	luku = int(input("Luku: "))
	if luku == 0:
		break
	luvut += f"{luku} "
	kierros += 1
	summa += luku
	if luku > 0:
		positiivinen += 1
	else:
		negatiivinen += 1

keskiarvo = summa / kierros
	
print(f"Lukuja yhteensä {kierros}")
print(f"Lukujen summa {summa}")
print(f"Lukujen keskiarvo {keskiarvo}")
print(f"Positiivisia {positiivinen}")
print(f"Negatiivisia {negatiivinen}")
