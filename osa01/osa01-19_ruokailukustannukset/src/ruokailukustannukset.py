# Kirjoita ratkaisu tähän
kerta = float(input("Montako kertaa viikossa syöt Unicafessa?"))
hinta = float(input("Unicafe-lounaan hinta?"))
raha = float(input("Paljonko käytät viikossa ruokaostoksiin?"))

viikko = kerta * hinta + raha

print(f"Kustannukset keskimäärin:\n Päivässä {viikko/7} euroa\nViikossa {viikko} euroa")