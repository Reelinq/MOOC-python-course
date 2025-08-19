
ika = int(input("Kerro ikäsi: "))

if ika < 5 and ika >= 0:
    print("En usko, että osaat kirjoittaa...")

elif ika < 0 or ika > 100:
    print("Taitaa olla virhe")

else:
    print(f"Ok, olet siis {ika}-vuotias")