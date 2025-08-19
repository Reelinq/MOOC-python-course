nimi = input("Kenelle teos omistetaan: ")
teksti = input("Mihin kirjoitetaan: ")
with open (teksti, "w") as tiedosto:
	tiedosto.write("Hei " + nimi + ", toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi")