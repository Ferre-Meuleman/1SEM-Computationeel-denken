user_input = int(input("Give number to check up to for prime numbers: "))
Primes = []
            
for num in range(1, user_input+1):
    prime = True
    for i in range(2, num):
        if (num % i == 0):
            prime = False
    if prime:
        Primes.append(num)           
         

for i in range(0,len(Primes)):
    print(f"{Primes[i]}",end=" ")