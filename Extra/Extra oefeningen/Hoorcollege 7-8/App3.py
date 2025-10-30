def abs(x: float) -> float:
    if x < 0:
        return -x
    else:
        return x
    
def main():
    print(abs(-5.3))  # Verwachte output: 5.3
    print(abs(3.7))   # Verwachte output: 3.7
    print(abs(0.0))   # Verwachte output: 0.0

if __name__ == "__main__":
    main()