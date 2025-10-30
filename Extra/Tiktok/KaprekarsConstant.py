num = int(input("input number: "))
count = 0

while num != 6174:
    digits = [int(d) for d in str(num)]

    ascending_digits = sorted(digits)
    descending_digits = sorted(digits, reverse=True)

    ascending_num = int("".join(map(str, ascending_digits)))
    descending_num = int("".join(map(str, descending_digits)))

    num = descending_num - ascending_num
    count += 1
    print(num)


print(num, count)
