from Tempdata import MinimumTemperaturen, MaximumTemperaturen
AANTAL_DAGEN = 365


def printGegevensOverPeriode(minTemperaturen, maxTemperaturen, startDag, eindDag):
    print("Gegevens over de hittegolfperiode:")
    for i in range(startDag, eindDag):
        print(
            f"Dag {i}: Min Temp = {minTemperaturen[i]}°C, Max Temp = {maxTemperaturen[i]}°C")


def zoekHitteGolven(minTemperaturen: list, maxTemperaturen: list):
    continuesHitteDagen = 0
    continuesWarmdays = 0
    startdate = 0
    heatcheck = False

    for day in range(len(minTemperaturen)):
        if maxTemperaturen[day] < 25:
            continuesWarmdays = 0
            continuesHitteDagen = 0
            heatcheck = False
            continue

        continuesWarmdays += 1
        startdate = day if continuesWarmdays == 1 else startdate
        if maxTemperaturen[day] >= 30:
            continuesHitteDagen += 1
            if continuesHitteDagen == 3:
                print(f"Hittegolf gestart op dag {startdate}")
                heatcheck = True

        if continuesWarmdays >= 5 and heatcheck:
            enddate = day
            printGegevensOverPeriode(minTemperaturen, maxTemperaturen, startdate, enddate)
            heatcheck = False


def main():
    minimumTemperaturen = MinimumTemperaturen
    maximumTemperaturen = MaximumTemperaturen
    zoekHitteGolven(minimumTemperaturen, maximumTemperaturen)


if __name__ == "__main__":
    main()
