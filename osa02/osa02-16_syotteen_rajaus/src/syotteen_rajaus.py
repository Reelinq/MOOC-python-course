from math import sqrt
# Kirjoita ratkaisu tähän
while True:
      luku = float(input("Syötä luku: "))
      if luku > 0:
             print(sqrt(luku))
      elif luku < 0:
              print("Epäkelpo luku")
      elif luku == 0:
             break
print("Lopetetaan...")

