from math import sqrt

Side1 = int(input("Give the first side of the thriangle: "))
Side2 = int(input("Give the second side of the thriangle: "))
Side3 = int(input("Give the third side of the thriangle: "))

Sides = [Side1, Side2, Side3]
Sides.sort()

if pow(Sides[0],2) + pow(Sides[1],2) == pow(Sides[2],2):
    print("The given sides are form a triangle with a 90 corner")
else:
    print("The given sides are form not form a triangle with a 90 corner")
