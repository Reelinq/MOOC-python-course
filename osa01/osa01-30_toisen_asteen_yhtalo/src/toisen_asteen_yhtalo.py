from math import sqrt

a = int(input("Anna a:"))
b = int(input("Anna b:"))
c = int(input("Anna c:"))

sol1 = (-b-sqrt(b**2 - 4*a*c))/(2*a)
sol2 = (-b+sqrt(b**2 - 4*a*c))/(2*a)

print(f"Juuret ovat {sol1,sol2}")