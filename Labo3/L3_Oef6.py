def main():
    tuple1 = (12, 40, 8, 20, 7, "John", 10.2)
    # geef alle waarden van deze tuple weer
    print(*tuple1, sep=", ")

    # geef de lengte van de tuple weer  resultaat : 7
    print(len(tuple1))

    # geef element met index 2 weer  resultaat : 8
    print(tuple1[2])
    """
    # vervang waarde van element met index 1, door waarde 4    
    tuple1[1] = 4
    
    --> dit is onmoglijk eenmaal tuple aangemaakt is die onveranderbaar
    """


if __name__ == "__main__":
    main()
