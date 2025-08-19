# Kirjoita ratkaisu tähän
asti = int(input("Mihin asti?"))
luku = 2
kerroin = 1
tarina = "1"

while asti > kerroin:
	tarina += f" + {luku}"
	kerroin += luku
	luku += 1
	
print(f"Laskettiin {tarina} = {kerroin}")