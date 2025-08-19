class Havaintoasema:
	def __init__(self, nimi: str):
		self.__nimi = nimi
		self.__lista = []
		self.__havaintojen_maara = 0

	def lisaa_havainto(self, havainto: str):
		self.__lista.append(havainto)
		self.__havaintojen_maara += 1

	def viimeisin_havainto(self):
		if self.__lista == []:
			return ""
		else:
			return self.__lista[-1]

	def havaintojen_maara(self):
		return self.__havaintojen_maara

	def __str__(self):
		return f"{self.__nimi}, {self.__havaintojen_maara} havaintoa"

if __name__ == "__main__":
	asema = Havaintoasema("Kumpula")
	asema.lisaa_havainto("Sadetta 10mm")
	asema.lisaa_havainto("Aurinkoista")
	print(asema.viimeisin_havainto())

	asema.lisaa_havainto("Ukkosta")
	print(asema.viimeisin_havainto())

	print(asema.havaintojen_maara())
	print(asema)