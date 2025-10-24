def bepaal_grootste(list: list):
    biggest = 0

    for i in range(0, len(list)):
        for j in range(0, len(list[i])):
            if list[i][j] > biggest:
                biggest = list[i][j]

    return biggest


def bepaal_frequentie(list: list, number: int):
    frequentie = 0

    for i in range(0, len(list)):
        for j in range(0, len(list[i])):
            if list[i][j] == number:
                frequentie += 1

    return frequentie


def get_pos(list: list, number: int):
    pos = []

    for i in range(0, len(list)):
        for j in range(0, len(list[i])):
            if list[i][j] == number:
                pos.append([i, j])

    return pos


def main():
    list2 = [[12, 40, 8, 20, 7], [10, 4, 3, 20, 40]]
    # geef alle waarden van deze lijst weer op het scherm
    print(*list2[0], sep=" ", end="\n")
    print(*list2[1], sep=" ")

    # geef het aantal rijen van de lijst weer  resultaat : 2
    print(len(list2))

    # geef het aantal kolommen van de lijst weer resultaat : 5
    print(len(list2[0]))

    # Bepaal het grootste getal in deze lijst  resultaat : 40 getatal gebruik een zelf geschreven functie : bepaal_grootste ( ).
    biggest = bepaal_grootste(list2)
    print(biggest)

    # Bepaal hoeveel keer dit grootste getal voorkomt in de lijst. Gebruik een zelf geschreven functie : bepaal_frequentie ( ).
    print(bepaal_frequentie(list2, biggest))

    # Bepaal eveneens op welke positie(s) dit grootste voorkomt in de lijst.
    pos = get_pos(list2, biggest)
    for i in pos:
        print(f"rij : {i[0]} en kolom : {i[1]}")


if __name__ == "__main__":
    main()
