num1 = int(input("Give first number in: "))
num2= int(input("Give second number in: "))

if num1 == num2:
    print(f"Both numbers are {num1}")

elif num1 < num2:
    print(f"The first number: {num1} is smaller than the second: {num2}")
    
else:
    print(f"The first number: {num1} is bigger than the second: {num2}")
    