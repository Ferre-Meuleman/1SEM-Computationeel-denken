number = int(input("Give a number: "))

number_str = str(number)
if number_str[0] == '-':
    aantal_cijfers = len(number_str) - 1
else:
    aantal_cijfers = len(number_str)
    
print(f"Het aantal cijfers is: {aantal_cijfers}")