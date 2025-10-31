numbers = []
number1 = int(input("Give a number: "))
number2 = int(input("Give a number: "))
number3 = int(input("Give a number: "))

numbers = [number1, number2, number3]

average = round(sum(numbers)/len(numbers),2)

print(f"The average of the given numbers is {round(average,2)}")