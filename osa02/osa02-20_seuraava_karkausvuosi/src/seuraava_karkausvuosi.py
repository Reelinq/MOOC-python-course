vuosi = int(input("Vuosi: "))
kvuosi = vuosi
while True:
    vuosi += 1
    if vuosi % 4 == 0 and vuosi % 100!= 0 or vuosi % 400 == 0:
        break
print(f"Vuotta {kvuosi}  seuraava karkausvuosi on {vuosi}")