numbers = []
correct = False

for i in range(0,3):
    numbers.append(int(input("give a number: ")))


small_to_big = sorted(numbers)
big_to_small = sorted(numbers, reverse=True)


if (small_to_big   == numbers) or (big_to_small == numbers):
    correct = True
    
print(correct)
    