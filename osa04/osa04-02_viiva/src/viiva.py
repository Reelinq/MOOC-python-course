# tee ratkaisu tänne
def viiva(leveys, merkkijono):
    if merkkijono == "":
        print("*" * leveys)
    else:
          print(merkkijono[0] * leveys)
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    viiva(5, "x")
