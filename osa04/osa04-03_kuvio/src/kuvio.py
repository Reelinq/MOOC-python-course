# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäendef viiva(koko, merkkijono):
def viiva(koko, merkkijono):
    if merkkijono == "":
        print("*" * koko)
    else:
          print(merkkijono[0] * koko)
          
def kuvio(koko, merkki, koko1, merkki1):
    pituus = 1
    pituus1 = 1
    while pituus <= koko:
        viiva(pituus, merkki)
        pituus += 1
    while pituus1 <= koko1:
        viiva(pituus -1, merkki1)
        pituus1 += 1
            

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kuvio(5, "x", 2, "o")
