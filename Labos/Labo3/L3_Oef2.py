def is_prime(num: int):
    prime = True
    for i in range(2, num):
        if (num % i == 0):
            prime = False
    if prime:
        return True
    return False


def main():
    user_input = int(input("Give number to check up to for prime numbers: "))
    primes = []

    for num in range(1, user_input+1):
        if is_prime(num):
            primes.append(num)

    print(*primes, sep=", ")


if __name__ == "__main__":
    main()
