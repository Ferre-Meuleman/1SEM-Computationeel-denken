def eval(x: float, polynoom: list) -> float:
    resultaat = 0
    for coeff in reversed(polynoom):
        resultaat = resultaat * x + coeff
    return resultaat


def main():
    example_polynoom = [2, -6, 2, -1]
    value = eval(3, example_polynoom)
    print(value)


if __name__ == "__main__":
    main()
