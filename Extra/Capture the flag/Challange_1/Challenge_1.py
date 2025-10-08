import random

def vul_plakboeken(aantal_kaarten=100):
    boek1 = set()
    boek2 = set()
    totaal_getrokken = 0

    # Eerst boek 1 vullen
    while len(boek1) < aantal_kaarten or len(boek2) < aantal_kaarten:
        kaart = random.randint(1, aantal_kaarten)
        if kaart not in boek1:
            boek1.add(kaart)
        elif kaart not in boek2:
            boek2.add(kaart)
        totaal_getrokken += 1



    return totaal_getrokken

def simulatie(aantal_runs=100000, aantal_kaarten=100):
    resultaten = [vul_plakboeken(aantal_kaarten) for _ in range(aantal_runs)]
    gemiddelde = sum(resultaten) / aantal_runs
    return gemiddelde


# Uitvoeren van de simulatie
gemiddeld_aantal = simulatie()
print(f"Gemiddeld aantal kaarten nodig: {gemiddeld_aantal:.4f}")