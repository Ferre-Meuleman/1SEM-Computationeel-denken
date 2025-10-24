num = int(input("Give a number: "))

i = 2

print("Delers: ")
print(1, end=' ')

for i in range(2, num + 1):
    if not num % i:
        print(i, end=' ')