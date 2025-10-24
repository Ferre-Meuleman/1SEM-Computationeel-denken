pos_sum = 0
neg_sum = 0

while True:
    num = int(input("Give a pos or neg integer (0 to stop): "))
    if num == 0:
        break
    elif num > 0:
        pos_sum += num
    else:
        neg_sum += num

print(f"Sum of positive numbers: {pos_sum}")
print(f"Sum of negative numbers: {neg_sum}")
