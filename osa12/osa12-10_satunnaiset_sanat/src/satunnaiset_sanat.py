def sanageneraattori(kirjaimet: str, pituus: int, maara: int):
	return (kirjaimet[i : i + pituus] for i in range(maara))
