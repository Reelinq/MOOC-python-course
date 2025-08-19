# tee ratkaisu tänne
def risunelio(pituus):
    for i in range(pituus):
        tulos = "#" * pituus
        print(tulos)
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)