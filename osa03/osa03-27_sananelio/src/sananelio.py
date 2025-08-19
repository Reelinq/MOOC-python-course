# tee ratkaisu tänne
def nelio(jono, luku):
    lista = []
    x = 0
    for i in jono:
        lista += i
    for y in range(luku):
        for z in range(luku):
            i = lista[x]
            print(i, end=(""))
            x += 1
            if x == len(lista):
                x = 0
        print()

if __name__ == "__main__":
    nelio("ab", 3)