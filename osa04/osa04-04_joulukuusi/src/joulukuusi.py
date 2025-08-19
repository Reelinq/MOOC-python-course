# tee ratkaisu tänne
def joulukuusi(pituus):
    i = 1
    kertaa = 1
    kerroin = pituus
    print("joulukuusi!")
    while i <= pituus:
        vali = pituus - i
        väli = " " * vali
        merkki = "*" * kertaa
        print(väli + merkki)
        kerroin -= 1
        i += 1
        kertaa += 2
    x = pituus - 1
    väli = " " * x
    print(f"{väli}*")
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    joulukuusi()