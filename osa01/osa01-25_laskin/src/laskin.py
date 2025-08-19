# Kirjoita ratkaisu tähän
luku1 = int(input("Anna luku 1: "))
luku2 = int(input("Anna luku 2: "))
komento = input("Anna komento: ")
if komento == "summa":
    print(f"{luku1} + {luku2} = {luku1 + luku2}")
if komento == "tulo":
    print(f"{luku1} * {luku2} = {luku1 * luku2}")
if komento == "erotus":
    print(f"{luku1} - {luku2} = {luku1 - luku2}")
