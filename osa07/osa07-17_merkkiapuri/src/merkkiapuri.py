def vaihda_koko(merkkijono: str):
    uusi_merkkijono = ''
    for i in merkkijono:
        if i.islower():
            uusi_merkkijono += i.upper()
        else:
            uusi_merkkijono += i.lower()
    return uusi_merkkijono

def puolita(merkkijono: str):
	p1 = merkkijono[0:len(merkkijono)//2]
	p2 = merkkijono[len(merkkijono)//2:]
	return p1, p2

def poista_erikoismerkit(merkkijono: str):
	for i in merkkijono:
		if not i.isalnum() and not i.isspace():
			merkkijono = merkkijono.replace(i, "")
	return merkkijono

if __name__ == '__main__':
	import merkkiapuri

	mjono = "Moi kaikki!"

	print(merkkiapuri.vaihda_koko(mjono))

	p1, p2 = merkkiapuri.puolita(mjono)

	print(p1)
	print(p2)

	m2 = merkkiapuri.poista_erikoismerkit("Tämä on testi, katsotaan miten käy!!!11!")
	print(m2)