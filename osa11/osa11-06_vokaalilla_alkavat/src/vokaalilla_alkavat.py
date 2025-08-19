def vokaalilla_alkavat(sanat: list):
	return [sana for sana in sanat if sana.lower()[0] in ("a", "e", "i", "o", "u", "y", "ä", "ö")]
