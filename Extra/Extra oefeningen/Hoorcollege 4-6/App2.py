import numpy as np

# Invoer
x = float(input("Geef x: "))
y = float(input("Geef y: "))

# Bereken r en θ
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)  

# Toon resultaat
print(f"r = {r:.4f}")
print(f"θ = {theta:.4f} rad")  
print(f"θ = {np.degrees(theta):.2f}°")  
