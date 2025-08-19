def koe_ja_harjoitukset(inpt):
    jaettu = inpt.split(" ")
    return int(jaettu[0]), int(jaettu[1])

def harjoituspisteet(maara):
    return maara // 10

def arvosana(pisteet):
    lista = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if pisteet >= lista[i]:
            return i

def main():
    pisteet = []
    arvosanat = [0] * 6
    while True:
        inpt = input("Koepisteet ja harjoitusten määrä: ")
        if len(inpt) == 0:
            break

        koe, harjoitukset = koe_ja_harjoitukset(inpt)
        harjoitus_pisteet = harjoituspisteet(harjoitukset)
        kokonaispistemaara = koe + harjoitus_pisteet

        pisteet.append(kokonaispistemaara)
        arvo = arvosana(kokonaispistemaara)
        if koe < 10:
            arvo = 0
        arvosanat[arvo] += 1

    lapipaasy = 100 * (len(pisteet) - arvosanat[0]) / len(pisteet)

    print("Tilasto:")
    print(f"Pisteiden keskiarvo: {sum(pisteet) / len(pisteet):.1f}")
    print(f"Hyväksymisprosentti: {lapipaasy:.1f}")
    print("Arvosanajakauma:")
    for i in range(5, -1, -1):
        tahdet = "*" * arvosanat[i]
        print(f"  {i}: {tahdet}")

main()
