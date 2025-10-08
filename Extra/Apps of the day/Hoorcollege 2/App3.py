import math

print("Functie is als volged Ax² + Bx + C")
A = float(input("Voer A in: "))
B = float(input("Voer B in: "))
C = float(input("Voer C in: "))

if A == 0:
    if B == 0:
        if C == 0:
            print("Er zijn oneindig veel oplossingen (alle x voldoen).")
        else:
            print("Er zijn geen oplossingen (de vergelijking is ongeldig).")
    else:
        x = -C / B
        print(f"Er is één oplossing: x = {x}")
else:
    D = B**2 - 4*A*C

    if D < 0:
        print("Er zijn geen reële oplossingen.")
    elif D == 0:
        x = -B / (2*A)
        print(f"Er is één oplossing: x = {x}")
    else:
        x1 = (-B + math.sqrt(D)) / (2*A)
        x2 = (-B - math.sqrt(D)) / (2*A)
        print("Er zijn twee oplossingen:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
