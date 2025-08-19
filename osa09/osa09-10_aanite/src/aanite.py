class Aanite:
	def __init__(self, pituus: int):
		self.__pituus = pituus
		if pituus < 0:
			raise ValueError("Pituus ei saa olla negatiivinen")

	@property
	def pituus(self):
		return self.__pituus
	
	@pituus.setter
	def pituus(self, pituus: int):
		if pituus >= 0:
			self.__pituus = pituus
		else:
			raise ValueError("Pituus ei saa olla negatiivinen")