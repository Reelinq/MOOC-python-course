# Kirjoita ratkaisu tähän
lampotila = int(input("Anna lämpötila (F):"))
print(f"{lampotila} fahrenheit-astetta on {(lampotila - 32) * 5 / 9} celsius-astetta")
if lampotila < 32:
    print("Paleltaa!")