# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(koko, merkkijono):
    if merkkijono == "":
        print("*" * koko)
    else:
          print(merkkijono[0] * koko)

def kolmio(koko):
    pituus = 1
    while pituus <= koko:
        viiva(pituus, "#")
        pituus += 1
        

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kolmio(5)
