def jarjesta_pisteiden_mukaan(alkiot: list):
	def pistejarjestys(alkio: dict):
		return alkio.get("pisteet")
	return sorted(alkiot, key=pistejarjestys, reverse=True)