class Palloilija:
    def __init__(self, nimi: str, pelinumero: int, maalit: int, syotot: int, minuutit: int):
        self.nimi = nimi
        self.pelinumero = pelinumero
        self.maalit = maalit
        self.syotot = syotot
        self.minuutit = minuutit

    def __str__(self):
        return (f'Palloilija(nimi={self.nimi}, pelinumero={self.pelinumero}, '
            f'maalit={self.maalit}, syotot={self.syotot}, minuutit={self.minuutit})')

# TEE RATKAISUSI TÄHÄN:
def eniten_maaleja(palloilijat: list):
    kasitelty = sorted(palloilijat, key=lambda palloilija: palloilija.maalit)[-1]
    return kasitelty.nimi

def eniten_pisteita(palloilijat: list):
    kasittely = sorted(palloilijat, key=lambda palloilija: palloilija.maalit + palloilija.syotot)[-1]
    return kasittely.nimi, kasittely.pelinumero

def vahiten_minuutteja(palloilijat: list):
    return sorted(palloilijat, key=lambda palloilija: palloilija.minuutit)[0]