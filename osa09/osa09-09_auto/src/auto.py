class Auto:
	def __init__(self):
		self.__bensa = 0
		self.__ajetut_kilometrit = 0

	def tankkaa(self):
		self.__bensa = 60

	def aja(self, km: int):
		if self.__bensa >= km:
			self.__bensa -= km
			self.__ajetut_kilometrit += km
		else:
			self.__ajetut_kilometrit += self.__bensa
			self.__bensa = 0
	def __str__(self):
		return f"Auto: ajettu {self.__ajetut_kilometrit} km, bensaa {self.__bensa} litraa"


if __name__ == "__main__":
	auto = Auto()
	print(auto)
	auto.tankkaa()
	print(auto)
	auto.aja(20)
	print(auto)
	auto.aja(50)
	print(auto)
	auto.aja(10)
	print(auto)
	auto.tankkaa()
	auto.tankkaa()
	print(auto)