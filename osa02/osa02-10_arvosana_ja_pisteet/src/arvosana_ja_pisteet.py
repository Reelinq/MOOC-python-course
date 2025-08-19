p = int(input("Anna pistemäärä: "))

if p < 0 or p > 100:
    print ("mahdotonta!")

elif p < 50:
    print ("hylätty")

elif p > 49 and p < 60:
    print("Arvosana: 1")

elif p > 59 and p < 70:
    print("Arvosana: 2")

elif p > 69 and p < 80:
    print("Arvosana: 3")

elif p > 79 and p < 90:
    print("Arvosana: 4")

elif p > 89 and p <= 100:
    print("Arvosana: 5")