from math import sqrt

number = int(input("Give a number: "))

if number <=0:
    print("The given number will not work")
    quit()
    
else:
    root = sqrt(number)
    if root % 1 == 0:
        print(f"The given number ({number}) is the square of {root}")
    else:
        print(f"The given number ({number}) not a full square")