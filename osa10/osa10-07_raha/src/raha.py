class Raha:
	def __init__(self, eurot: int, sentit: int):
		self.__eurot = eurot
		self.__sentit = sentit
		self.__summa = "{0:00}.{1:02}".format(self.__eurot, self.__sentit)

	def __str__(self):
		return self.__summa + " eur"
	
	def __eq__(self, toinen):
		return self.__summa == toinen.__summa

	def __lt__(self, toinen):
		return self.__summa < toinen.__summa

	def __gt__(self, toinen):
		return self.__summa > toinen.__summa

	def __ne__(self, toinen):
		return self.__summa != toinen.__summa
	
	def __add__(self, toinen):
		vastaus = float(self.__summa) + float(toinen.__summa)
		return "{:.2f} eur".format(vastaus)
	
	def __sub__(self, toinen):
		vastaus = float(self.__summa) - float(toinen.__summa)
		if vastaus < 0:
			raise ValueError("Negatiivinen tulos ei ole sallittu")
		return "{:.2f} eur".format(vastaus)

if __name__ == "__main__":
	e1 = Raha(4, 5)
	e2 = Raha(2, 95)

	e3 = e1 + e2
	e4 = e1 - e2

	print(e1)
	print(e2)
	print(e3)
	print(e4)
