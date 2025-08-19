# Kirjoita ratkaisu tähän
list = []
while True:
	print(f"Lista on nyt {list}")
	kirjain = input("(l)isää, (p)oista vai e(x)it:")
	if kirjain == "l":
		lisaa = len(list) + 1
		list.append(lisaa)
	elif kirjain == "p":
		list.pop(-1)
	elif kirjain == "x":
		break
print("Moi!")