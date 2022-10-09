from cmath import sqrt

a = float(input("donner le coeficient a de l'equation: "))
b = float(input("donner le coeficient b de l'equation: "))
c = float(input("donner le coeficient c de l'equation: "))

delta = b**2 - 4*a*c

if delta == 0:
    print("la solution de l'equation est:", -b/(2*a))
elif delta > 0:
    print(
        f"les deux solutions sont: x1={(-b-sqrt(delta))/(2*a)} et x2={(-b+sqrt(delta))/(2*a)}")
else:
    print("l'equation n'a aucune solution dans R")
