import math

def CalcFunc(A: int, B: int, C: int):
    solutions: int = 0
    x1: float = 0
    x2: float = 0

    if A == 0:
        if B == 0:
            if C == 0:
                solutions = 0
            else:
                solutions = 0             
        else:
            x1 = -C / B
            solutions = 1
    else:        
        D = B**2 - 4 * A * C

        if D < 0:
            solutions = 0
        elif D == 0:
            x1 = -B / (2 * A)
            solutions = 1
        else:
            sqrt_D = math.sqrt(D)
            x1 = (-B + sqrt_D) / (2 * A)
            x2 = (-B - sqrt_D) / (2 * A)
            solutions = 2

        return solutions, x1, x2

def main():
    print("Functie is als volged Ax² + Bx + C")
    A = float(input("Voer A in: "))
    B = float(input("Voer B in: "))
    C = float(input("Voer C in: "))
    
    solutions, x1, x2 = CalcFunc(A, B, C)
        
    print(f"\nEr zijn {solutions} oplossingen:")
    print(f"x₁ = {x1 :.3f}")
    print(f"x₂ = {x2 :.3f}")


if __name__ == "__main__":
    main()