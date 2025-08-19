# tee ratkaisu tänne
def tuplaa_alkiot(luvut: list):
    uusilista = []
    for i in luvut:
        uusilista.append(i * 2)
    return uusilista

if __name__ == "__main__":
    luvut = [2, 4, 5, 3, 11, -4]
    tuplaluvut = tuplaa_alkiot(luvut)
    print("alkuperäinen:", luvut)
    print("tuplattu:", tuplaluvut)
