number = int(input("Give a number: "))

numbers = []
primenumber = []

i = 1
while number > len(numbers):
    numbers.append(i)
    i += 1
    
numbers.remove(1)

while len(numbers)!= 0:
    x = numbers[0]
    primenumber.append(x)
    i = 0
    while i < len(numbers):
        if numbers[i] % x == 0:
            numbers[i] = 1
        i += 1
    numbers = [i for i in numbers if i != 1]

print(primenumber)