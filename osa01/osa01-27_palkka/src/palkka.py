# Kirjoita ratkaisu tähän
tuntipalkka = float(input("Tuntipalkka: "))
tyotunnit = float(input("Työtunnit: "))
viikonpaiva = input("Viikonpäivä: ")

if viikonpaiva == "sunnuntai":
    print(f"Palkka {tuntipalkka * tyotunnit * 2} euroa")

else:
    print(f"Palkka {tuntipalkka * tyotunnit} euroa")