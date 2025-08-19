class ListaApuri:
	@classmethod
	def suurin_frekvenssi(cls, lista: list):
		laskin = 0
		num = 0

		for numero in lista:
			tama_num = lista.count(numero)
			if tama_num > laskin:
				laskin = tama_num
				num = numero
		return num

	@classmethod
	def tuplia(cls, lista: list):
		tuplea_yht = 0
		apu_list = []
		for numero in lista:
			if numero not in apu_list:
				tama_num = lista.count(numero)
				if tama_num >= 2:
					tuplea_yht += 1
				apu_list.append(numero)
		return tuplea_yht

if __name__ == "__main__":
	luvut = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
	print(ListaApuri.suurin_frekvenssi(luvut))
	print(ListaApuri.tuplia(luvut))
