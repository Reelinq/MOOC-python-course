# Kirjoita ratkaisu tähän
yritys = 0
while True:
    koodi = int(input("PIN-koodi: "))
    yritys += 1
    if koodi != 4321:
        print("Väärin")
    else:
        break
if yritys == 1:
    print("Oikein, tarvitsit vain yhden yrityksen!")
else:
     print(f"Oikein, tarvitsit {yritys} yritystä")

    