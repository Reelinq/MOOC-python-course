from datetime import datetime
paiva = int(input("Päivä: "))
kuukausi = int(input("Kuukausi: "))
vuosi = int(input("Vuosi: "))
nyt = datetime.now()
if vuosi < 2000:
	syntyma = datetime(vuosi, kuukausi, paiva)
	vuosituhat = datetime(1999, 12, 31)
	ika = (vuosituhat - syntyma).days
	print(f"Olit {ika} päivää vanha, kun vuosituhat vaihtui.")	
else:
	print("Et ollut syntynyt, kun vuosituhat vaihtui.")