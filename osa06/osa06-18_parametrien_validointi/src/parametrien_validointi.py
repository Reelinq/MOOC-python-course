def uusi_henkilo(nimi: str, ika: int):
	if nimi == "":
		raise ValueError("Nimi ei saa olla tyhjä")
	if " " not in nimi:
		raise ValueError("Nimen on oltava muodostonut vähintään kahdesta sanasta")
	if len(nimi) > 40:
		raise ValueError("Nimen pituus ei saa olla yli 40 merkkiä")
	if ika < 0:
		raise ValueError("Ikä ei voi olla negatiivinen")
	if ika > 150:
		raise ValueError("Ikä ei voi olla yli 150")
	return (nimi, ika)