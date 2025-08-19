# tee ratkaisu tänne
def keskiarvo(lista):
	i = 0
	sum = 0
	while i < len(lista):
		sum += lista[i]
		i += 1
	return sum/len(lista)
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = keskiarvo(lista) 
    print(tulos)
