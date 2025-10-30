import random


def gooi_dobbelstenen(aantal_worpen):
    aantal_keer_een = 0
    for _ in range(aantal_worpen):
        number = random.randint(1, 6)
        if number == 1:
            aantal_keer_een += 1

    return aantal_keer_een


def simulatie(aantal_simulaties):
    successen1 = 0
    successen2 = 0
    for _ in range(aantal_simulaties):
        worpen = gooi_dobbelstenen(6)
        meer_worpen = gooi_dobbelstenen(12)

        if worpen >= 1 and not meer_worpen >= 2:
            successen1 += 1
        else:
            successen2 += 1

    if successen1 > successen2:
        print("Het is waarschijnlijker om minstens 1 keer een 1 te gooien bij 6 worpen.")
    else:
        print("Het is waarschijnlijker om minstens 2 keer een 1 te gooien bij 12 worpen.")

    return 1


def main():
    simulatie(10000)


if __name__ == "__main__":
    main()
