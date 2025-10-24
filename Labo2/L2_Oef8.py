user_input = int(input("Give number to check for prime number: "))

is_prime = True
for i in range(2, user_input):
    if int(user_input) % i == 0 :
        is_prime = False
        break 

if is_prime:
   print("Your number is a prime number")
else:
   print("your number is not a prime number")