number = input("Give me a 10 digit ISBN number: ")
sum = 0

for i in range(0, len(number)):
    if number[-i] == 'X':
        sum = 10 * (i) + sum
    else:
        sum = int(number[-i]) * (i) + sum

if sum % 11 == 0:
    print(f"The number {number} is a valid ISBN number")

else:
    print(f"The number {number} is not a valid ISBN number")
