# Kirjoita ratkaisu tähän
lampotila = int(input("Lämpötila?"))
saa = input("Sataako (kyllä/ei)")

if 21 <= lampotila:
    print("Pue housut ja t-paita")

if 16 <= lampotila <= 20:
    print("Pue housut ja t-paita")
    print("Ota myös pitkähihainen paita")

if 11 <= lampotila <= 15:
    print("Pue housut ja t-paita")
    print("Ota myös pitkähihainen paita")

if 6 <= lampotila <= 10:
    print("Pue päälle takki")
    print("Ota myös pitkähihainen paita")
    print("Pue housut ja t-paita")

if lampotila <= 5:
    print("Pue housut ja t-paita")
    print("Ota myös pitkähihainen paita")
    print("Pue päälle takki")
    print("Suosittelen lämmintä takkia")
    print("Kannattaa ottaa myös hanskat")

if saa == "kyllä":
    print("Muista sateenvarjo!")