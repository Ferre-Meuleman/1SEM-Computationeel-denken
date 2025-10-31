lowest_number = 0
highest_number = 0

while True:
    number = int(input("Give a pos or neg integer: "))
    if number == 0:
        break
    else:
        if number > highest_number:
            highest_number = number
        elif number < lowest_number:
            lowest_number = number    


print(f"Lowest number: {lowest_number}")
print(f"Highest number: {highest_number}")