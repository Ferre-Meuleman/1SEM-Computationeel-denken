from random import randint

number = randint(0,1000)

guess = 1001
guesses = 0

while guess != number:
    guesses += 1
    guess = int(input("Guess the random number: "))
    if guess == number:
        break
    elif guess > number:
        print(f"The number is lower than {guess}")    
    else:
        print(f"The number is higher than {guess}")  
        
print(f"It took {guesses} to guess the number {number}")