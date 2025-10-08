def lees_complex(nr):
    s = input(f"Voer complex getal {nr} in (vorm: a + bi of a - bi): ").replace(" ", "")
    if "i" not in s:
        return (float(s), 0.0)
    s = s.replace("i", "")
    for i in range(1, len(s)):
        if s[i] in "+-" and i != 0:
            a = float(s[:i])
            b = float(s[i:])
            return (a, b)
    return (0.0, float(s))

a = lees_complex(1)
b = lees_complex(2)

som = (a[0] + b[0], a[1] + b[1])
product = (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])

print(f"Eerste complex getal: {a[0]} + ({a[1]})i")
print(f"Tweede complex getal: {b[0]} + ({b[1]})i")
print(f"Som: {som[0]} + ({som[1]})i")
print(f"Product: {product[0]} + ({product[1]})i")
