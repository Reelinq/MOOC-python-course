def suodata_kielletyt(merkkijono: str, kielletyt: str):
	return "".join(["" if sana in kielletyt else sana for sana in merkkijono])
