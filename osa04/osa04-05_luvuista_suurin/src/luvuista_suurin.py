# tee ratkaisu tänne
def luvuista_suurin(a, b, c):
    if a >= b >= c or a >= c >= b:
        return a
    elif b >= c >= a or b >= a >= c:
        return b
    else:
        return c

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    suurin = luvuista_suurin(5, 4, 8)
    print(suurin)