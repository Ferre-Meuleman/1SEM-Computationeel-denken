n = int(input("Give amount of Fibonacci steps: "))

if n <= 0:
    quit()
elif n == 1:
    print(1)
else:
    a, b = 1, 1
    print(a, b, end=' ')
    for i in range(2, n):
        a, b = b, a + b
        print(b, end=' ')
