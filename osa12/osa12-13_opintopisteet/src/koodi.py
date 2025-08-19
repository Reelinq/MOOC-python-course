from functools import reduce

class Suoritus:
    def __init__(self, kurssi: str, arvosana: int, opintopisteet: int):
        self.kurssi = kurssi
        self.arvosana = arvosana
        self.opintopisteet = opintopisteet

    def __str__(self):
        return f"{self.kurssi} ({self.opintopisteet} op) arvosana {self.arvosana}"

# Tee ratkaisusi tähän:


def kaikkien_opintopisteiden_summa(suoritukset: list):
    return reduce(lambda summa, alkio: summa + alkio.opintopisteet, suoritukset, 0)

def hyvaksyttyjen_opintopisteiden_summa(suoritukset: list):
    return reduce(lambda summa, alkio: summa + alkio.opintopisteet, filter(lambda a: a.arvosana > 0, suoritukset), 0)

def keskiarvo(suoritukset: list):
    return reduce(lambda summa, alkio: summa + alkio.arvosana, filter(lambda a: a.arvosana > 0, suoritukset), 0) / len(list(filter(lambda a: a.arvosana > 0, suoritukset)))
