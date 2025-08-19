# tee ratkaisu tänne
def shakkilauta(kerroin):
    i = 0
    while i < kerroin:
        x = 0
        while x < kerroin:
            if (x + i) % 2 == 0:
                print("1", end="")
            else:
                print("0", end="")
            x += 1
        print()
        i += 1
# kokeillaan funktiota kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    shakkilauta(3)
