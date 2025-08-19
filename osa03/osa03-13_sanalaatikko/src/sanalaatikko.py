# Kirjoita ratkaisu tähän
sana = input("Sana: ")
vali1 = int((28 - len(sana))/2)
vali2 = 28 - len(sana) -vali1
if (vali1+vali2) % 2 == 0:
	vali1 += 1
	vali2 -= 1

print("*"*30)
print("*" + " "*vali1 + sana + " "*vali2 + "*")
print("*"*30)