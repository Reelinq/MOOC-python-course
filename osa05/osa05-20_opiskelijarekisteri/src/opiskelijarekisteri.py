def lisaa_opiskelija(opiskelijat, opiskelija):
    opiskelijat[opiskelija.lower()] = {}

def tulosta(opiskelijat, opiskelija):
    oppilas = opiskelijat.get(opiskelija.lower())
    if opiskelija in opiskelijat:
        print(opiskelija + ":")
        if oppilas:
            print(" suorituksia", len(oppilas), "kurssilta:")
            for aine, arvosana in oppilas.items():
                print(" ",aine, arvosana)
            keskiarvo = sum(oppilas.values()) / len(oppilas)
            print(" keskiarvo", keskiarvo)
        else:
            print(" ei suorituksia")
    else:
        print("ei löytynyt ketään nimellä " + opiskelija)

def lisaa_suoritus(opiskelijat, opiskelija, kurssi: tuple):
    oppilas = opiskelijat[opiskelija.lower()]
    if kurssi[1] == 0:
        return
    if kurssi[1] > oppilas.get(kurssi[0], 0):
        oppilas[kurssi[0]] = kurssi[1]

def kooste(opiskelijat):
    print("opiskelijoita", len(opiskelijat))
    suurin, paras_opiskelija = 0, ""
    for opiskelija, oppilas in opiskelijat.items():
        if len(oppilas) > suurin:
            suurin, paras_opiskelija = len(oppilas), opiskelija
    print("eniten suorituksia", suurin, paras_opiskelija)
    paras_keskiarvo = (0, "")
    for opiskelija, oppilas in opiskelijat.items():
        if oppilas:
            keskiarvo = sum(oppilas.values()) / len(oppilas)
            if keskiarvo > paras_keskiarvo[0]:
                paras_keskiarvo = (keskiarvo, opiskelija)
    print("paras keskiarvo", paras_keskiarvo[0], paras_keskiarvo[1])


if __name__ == "__main__":
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "emilia")
    lisaa_opiskelija(opiskelijat, "pekka")
    lisaa_suoritus(opiskelijat, "emilia", ("ohpe", 4))
    lisaa_suoritus(opiskelijat, "emilia", ("ohpe", 5))
    lisaa_suoritus(opiskelijat, "pekka", ("tira", 3))
    lisaa_suoritus(opiskelijat, "pekka", ("lama", 0))
    lisaa_suoritus(opiskelijat, "pekka", ("tira", 2))
    lisaa_suoritus(opiskelijat, "pekka", ("jtkt", 1))
    lisaa_suoritus(opiskelijat, "pekka", ("ohtu", 3))
    kooste(opiskelijat)
    kooste(opiskelijat)