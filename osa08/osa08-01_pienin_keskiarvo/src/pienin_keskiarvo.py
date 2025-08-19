def lasku(sanakirja: dict):
	list = []
	for i in sanakirja.values():
		list.append(i)
	return sum(list[1:]) / 3


def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):

	summa1 = lasku(henkilo1)
	summa2 = lasku(henkilo2)
	summa3 = lasku(henkilo3)

	if min(summa1, summa2, summa3) == summa1:
		return henkilo1
	if min(summa1, summa2, summa3) == summa2:
		return henkilo2
	if min(summa1, summa2, summa3) == summa3:
		return henkilo3
