def get_deviders(num: int):
    delers = []
    for i in range(1, num + 1):

        if num % i == 0:
            delers.append(i)
            print(f"{num % i} , {i}")

    return delers


def main():
    user_input = int(input("Give number to check if it is a perfect umber: "))
    delers = get_deviders(user_input)

    if sum(delers[:-1]) == user_input:
        print(f"Your number: {user_input} is a perfect number with deviders:")
        print(*delers, sep=", ")
    else:
        print(f"Your number: {user_input} is not a perfect number")


if __name__ == "__main__":
    main()
