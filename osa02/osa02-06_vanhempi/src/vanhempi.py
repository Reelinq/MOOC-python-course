# Kirjoita ratkaisu tähän
nimi1 = input("Henkilö 1:\nNimi: ")

ika1 = int(input("Ikä: "))

nimi2 = input("Henkilö 2:\nNimi: ")

ika2 = int(input("Ikä: "))

if ika1 > ika2:
    print(f"Vanhempi on {nimi1}")

elif ika1 < ika2:
    print(f"Vanhempi on {nimi2}")

elif ika1 == ika2:
    print(f"{nimi1} ja {nimi2} ovat yhtä vanhoja")