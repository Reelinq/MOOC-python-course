# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(koko, merkkijono):
    if merkkijono == "":
        print("*" * koko)
    else:
          print(merkkijono[0] * koko)
          
def risunelio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    i = 1
    while i <= koko:
          viiva(koko, "#")
          i += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)
