# Tee ratkaisusi tähän:
class  Lukutilasto:
    def __init__(self):
        self.lukuja = 0
        self.lisatyt_luvut = 0

    def lisaa_luku(self, luku:int):
        self.lukuja += luku
        self.lisatyt_luvut += 1

    def lukujen_maara(self):
        return self.lisatyt_luvut

    def summa(self):
        return self.lukuja

    def keskiarvo(self):
        if self.lukuja and self.lisatyt_luvut > 0:
            return self.lukuja / self.lisatyt_luvut

print("Anna lukuja:")
tilasto = Lukutilasto()
parillinen_tilasto = Lukutilasto()
pariton_tilasto = Lukutilasto()
while True:
    kysymys = int(input())
    if kysymys == -1:
        break
    tilasto.lisaa_luku(kysymys)
    if kysymys % 2 == 0:
        parillinen_tilasto.lisaa_luku(kysymys)
    else:
        pariton_tilasto.lisaa_luku(kysymys)
print("Summa:", tilasto.summa())
print("Keskiarvo:", tilasto.keskiarvo())
print("Parillisten summa:", parillinen_tilasto.summa())
print("Parittomien summa:", pariton_tilasto.summa())