def sulut_tasapainossa(merkkijono: str):
	if len(merkkijono) == 0:
		return True
	if merkkijono == ")" or merkkijono == "(" or merkkijono == "[" or merkkijono == "]":
		return False
	if merkkijono[0] == "(" and merkkijono[-1] == ")":
		return sulut_tasapainossa(merkkijono[1:-1])
	if merkkijono[0] == "[" and merkkijono[-1] == "]":
		return sulut_tasapainossa(merkkijono[1:-1])
	if merkkijono[0] == "(":
		return sulut_tasapainossa(merkkijono[0:-1])
	if merkkijono[-1] == ")":
		return sulut_tasapainossa(merkkijono[1:])
	if merkkijono[0] == "[":
		return sulut_tasapainossa(merkkijono[0:-1])
	if merkkijono[-1] == "]":
		return sulut_tasapainossa(merkkijono[1:])
	
	return sulut_tasapainossa(merkkijono[1:-1])
	
