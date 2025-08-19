def kaanna(sanakirja: dict):
    uusi_sanakirja = {}
    for i, arvo in sanakirja.items():
        uusi_sanakirja[arvo] = i
    sanakirja.clear()
    sanakirja.update(uusi_sanakirja)


if __name__ == "__main__":
    s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
    kaanna(s)
    print(s)
