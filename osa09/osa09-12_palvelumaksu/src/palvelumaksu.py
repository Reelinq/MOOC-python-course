class Pankkitili:
	def __init__(self,  tilinomistaja: str, tilinumero: str, saldo: float):
		self.__tiliomistaja = tilinomistaja
		self.__tilinumero = tilinumero
		self.saldo = saldo

	def talleta(self, summa: float):
		self.saldo += summa
		self.__palvelumaksu()

	def nosta(self, summa: float):
		self.saldo -= summa
		self.__palvelumaksu()

	def saldo(self):
		return self.saldo
	
	def __palvelumaksu(self):
		prosentti = self.saldo / 100
		self.saldo -= prosentti

if __name__ == "__main__":
	tili = Pankkitili("Raimo Rahakas", "12345-6789", 1000)
	tili.nosta(100)
	print(tili.saldo)
	tili.talleta(100)
	print(tili.saldo)
