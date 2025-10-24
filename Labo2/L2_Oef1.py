num = int(input("Give a number: "))

print("Delers: ")
print(1, end=' ')

i = 2
while i <= num:
    if not num % i:
        print(i, end=' ')
        
    i += 1