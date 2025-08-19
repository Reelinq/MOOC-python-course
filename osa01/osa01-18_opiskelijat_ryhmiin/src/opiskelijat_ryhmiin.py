# Kirjoita ratkaisu tähän
opiskelija = int(input("Montako opiskelijaa?"))
ryhma = int(input("Mikä on ryhmän koko?"))

if opiskelija % ryhma == 0:
    print(f"Ryhmien määrä: {opiskelija // ryhma}")
else:
    print(f"Ryhmien määrä: {opiskelija // ryhma+1}")
