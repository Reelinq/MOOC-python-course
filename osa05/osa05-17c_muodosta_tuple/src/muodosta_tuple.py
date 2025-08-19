# tee ratkaisu tänne
def tee_tuple(x: int, y: int, z: int):
	if x > y > z:
		b = x
		a = z
	elif x > z > y:
		b = x
		a = y
	elif y > z > x:
		b = y
		a = x
	elif y > x > z:
		b = y
		a = z
	elif z > y > x:
		b = z
		a = x
	elif z > x > y:
		b = z
		a = y
	c = x + y + z
	tuple = (a, b, c)
	return tuple


if __name__ == "__main__":
	print(tee_tuple(5, 3, -1))
