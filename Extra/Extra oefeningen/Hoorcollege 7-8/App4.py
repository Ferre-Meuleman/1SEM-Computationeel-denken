given_array = [3, 5, 2, 8, 6, 1, 4, 7]

def gemiddelde(arr: list) -> float:
    totaal = sum(arr)
    aantal = len(arr)
    return totaal / aantal

def main():
    print(gemiddelde(given_array))  # Verwachte output: 4.5

if __name__ == "__main__":
    main()