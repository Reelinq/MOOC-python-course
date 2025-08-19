# Kirjoita ratkaisu tähän
sanat = ""
sana2 = ""

while True:
    sana = input("Anna sana: ")
    if sana == "loppu" or sana == sana2:
        break

    sanat += sana + " "
    sana2 = sana

print(sanat)