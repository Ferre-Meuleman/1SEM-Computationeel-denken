t = float(input("Give the temparture [F]: "))
v = float(input("Give the speed [Mph]: "))

w = 35.74 + 0.6215 *t + (0.4275 * t - 35.75) * v ** 0.16

print(f"The feeling temprature is {w:.2f}F")