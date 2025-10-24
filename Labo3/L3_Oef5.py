def main():
    list1 = [12, 40, 8, 20, 7]
    # geef alle waarden van deze lijst weer:
    print(*list1, sep=", ")

    # geef de lengte van de lijst weer  resultaat : 5:
    print(len(list1))

    # geef element met index 2 weer  resultaat : 8:
    print(list1[2])

    # vervang waarde van element met index 1, door waarde 4:
    list1[1] = 4

    # voeg de waarde 3 achteraan toe:
    list1.append(3)

    # geef de lengte van de lijst weer  resultaat : 6:
    print(len(list1))

    # geef minimum van deze lijst weer  resultaat : 3:
    print(min(list1))

    # geef maximum van deze lijst weer  resultaat : 20:
    print(max(list1))

    # sommeer alle waarden van deze lijst resultaat : 54:
    print(sum(list1))

    # geef alle waarden van deze lijst onder elkaar weer:
    print(*list1, sep="\n")


if __name__ == "__main__":
    main()
