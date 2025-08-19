from datetime import datetime, timedelta

to = input("Tiedosto: ")
aloituspaiva = input("Aloituspäivä: ")
paivat = input("Montako päivää: ")
paivat = str(int(paivat) - 1)

aika = datetime.strptime(aloituspaiva, "%d.%m.%Y")
loppuaika = aika + timedelta(days=int(paivat))
print("Anna ruutuajat kunakin päivänä minuutteina (TV tietokone mobiililaite):")

r_summa = 0
lista = []
for i in range(int(paivat) + 1):
	tamapaiva = aika + timedelta(days=i)
	lista.append(tamapaiva)
	ruutuaika = input(f"Ruutuaika {tamapaiva.strftime('%d.%m.%Y')}: ")
	r = list(map(int, ruutuaika.split()))
	r_summa += sum(r)
	lista.append(r)

with open(to, "w") as tiedosto:
	print("Tiedoston sisältö on: \n")
	tiedosto.write(f"Ajanjakso: {aika.strftime('%d.%m.%Y')}-{loppuaika.strftime('%d.%m.%Y')}\n")
	tiedosto.write(f"Yht. minuutteja: {r_summa}\n")
	tiedosto.write(f"Keskim. minuutteja: {r_summa / (int(paivat) + 1)}\n")
	for i in range(0, len(lista), 2):
		tiedosto.write(f"{lista[i].strftime('%d.%m.%Y')}: {lista[i+1][0]}/{lista[i+1][1]}/{lista[i+1][2]}\n")
print(lista)
print(f"Tiedot tallennettu tiedostoon {to}")