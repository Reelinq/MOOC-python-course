class Lottorivi:
	def __init__(self, kierros: int, rivi: list):
		self.kierros = kierros
		self.rivi = rivi
	
	def osumien_maara(self, pelattu_rivi: list):
		return len([luku for luku in pelattu_rivi if luku in self.rivi])
	
	def osumat_paikoillaan(self, pelattu_rivi: list):
		return [luku if luku in self.rivi else -1 for luku in pelattu_rivi]