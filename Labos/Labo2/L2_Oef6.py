lowest_number :int
highest_number :int


while True:
    number = input("Give a pos or neg integer: ")
    if number == "":
        break
    else:
        if number > highest_number:
            highest_number = int(number)
        elif number < lowest_number:
            lowest_number = int(number)    

print(f"Lowest number: {lowest_number}")
print(f"Highest number: {highest_number}")