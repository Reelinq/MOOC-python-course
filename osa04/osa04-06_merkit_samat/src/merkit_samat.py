# tee ratkaisu tänne
def samat(merkkijono, a, b):
    if a >= len(merkkijono) or b >= len(merkkijono):
        return False
    return merkkijono[a] == merkkijono[b]

if __name__ == "__main__":
    print(samat("koodari", 1, 2))