# TEE RATKAISUSI TÄHÄN:

class Maksukortti:
    def __init__(self, saldo: float):
        self.saldo = saldo

    def lataa_rahaa(self, lisays: float):
        self.saldo += lisays

    def ota_rahaa(self, maara: float):
        if self.saldo >= maara:
            self.saldo -= maara
            return True
        else:
            return False
        # Toteuta metodi siten, että se ottaa kortilta rahaa vain, jos saldoa riittää
        # Onnistuessaan metodi palauttaa True ja muuten False

class Kassapaate:
    def __init__(self):
        # kassassa on aluksi 1000 euroa rahaa
        self.rahaa = 1000
        self.edulliset = 0
        self.maukkaat = 0

    def syo_edullisesti(self, maksu: float):
        hinta = 2.50
        if maksu >= hinta:
            self.rahaa += hinta
            self.edulliset += 1
            return maksu - hinta
        else:
            return maksu
        # Edullinen lounas maksaa 2.50 euroa
        # Kasvatetaan kassan rahamäärää edullisen lounaan hinnalla ja palautetaan vaihtorahat
        # Jos parametrina annettu maksu ei ole riittävän suuri, ei lounasta myydä ja metodi palauttaa koko summan

    def syo_maukkaasti(self, maksu: float):
        hinta = 4.30
        if maksu >= hinta:
            self.rahaa += hinta
            self.maukkaat += 1
            return maksu - hinta
        else:
            return maksu
        # Maukas lounas maksaa 4.30 euroa
        # Kasvatetaan kassan rahamäärää maukkaan lounaan hinnalla ja palautetaan vaihtorahat
        # Jos parametrina annettu maksu ei ole riittävän suuri, ei lounasta myydä ja metodi palauttaa koko summan

    def syo_edullisesti_kortilla(self, kortti:Maksukortti):
        hinta = 2.50
        if kortti.saldo >= hinta:
            kortti.saldo -= hinta
            self.edulliset += 1
            return True
        else:
            return False
        # Edullinen lounas maksaa 2.50 euroa
        # Jos kortilla on tarpeeksi rahaa, vähennetään hinta kortilta ja palautetaan True
        # Muuten palautetaan False

    def syo_maukkaasti_kortilla(self, kortti:Maksukortti):
        hinta = 4.30
        if kortti.saldo >= hinta:
            kortti.saldo -= hinta
            self.maukkaat += 1
            return True
        else:
            return False
        # Maukas lounas maksaa 4.30 euroa
        # Jos kortilla on tarpeeksi rahaa, vähennetään hinta kortilta ja palautetaan True
        # Muuten palautetaan False

    def lataa_rahaa_kortille(self, kortti: Maksukortti, summa: float):
        kortti.saldo += summa
        self.rahaa += summa


if __name__ == "__main__":
	exactum = Kassapaate()

	antin_kortti = Maksukortti(2)
	print(f"Kortilla rahaa {antin_kortti.saldo} euroa")

	tulos = exactum.syo_maukkaasti_kortilla(antin_kortti)
	print("Riittikö raha:", tulos)

	exactum.lataa_rahaa_kortille(antin_kortti, 100)
	print(f"Kortilla rahaa {antin_kortti.saldo} euroa")

	tulos = exactum.syo_maukkaasti_kortilla(antin_kortti)
	print("Riittikö raha:", tulos)
	print(f"Kortilla rahaa {antin_kortti.saldo} euroa")

	print("Kassassa rahaa", exactum.rahaa)
	print("Edullisia lounaita myyty", exactum.edulliset)
	print("Maukkaita lounaita myyty", exactum.maukkaat)
