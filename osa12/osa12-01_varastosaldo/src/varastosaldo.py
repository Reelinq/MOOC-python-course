def jarjesta_varastosaldon_mukaan(alkiot: list):
	def maarajarjestys(tuote: tuple):
		return tuote[2]
	return sorted(alkiot, key=maarajarjestys)