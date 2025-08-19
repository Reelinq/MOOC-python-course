# tee ratkaisu tänne
def poista_pienin(luvut: list):
    uusilista = []
    for i in luvut:
        uusilista.append(i)
    uusilista.sort()
    luku = uusilista[0]
    luvut.remove(luku)

if __name__ == "__main__":
    luvut = [2, 4, 6, 1, 3, 5]
    poista_pienin(luvut)
    print(luvut)
