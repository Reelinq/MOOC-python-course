def yleisimmat_sanat(tiedoston_nimi: str, raja: int):
	file = open(tiedoston_nimi).read().split()
	file_lista = ["".join([kirjain if kirjain not in ("!,:.?’â€™") else "" for kirjain in sana]) for sana in file]
	return {sana: file_lista.count(sana) for sana in file_lista if file_lista.count(sana) >= raja}
