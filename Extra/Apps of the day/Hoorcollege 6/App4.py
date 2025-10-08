def Countletter(letter : str, text: str):
    count: int = 0
    for x in text:
        if x.upper() == letter.upper(): 
            count += 1
    
    return count


def main():
    text = input("Give a string: ")
    letters = ['a', 'e', 'i', 'o', 'u']
    
    print("Here is the count of the letters in your string:")
    for letter in letters:
        count = Countletter(letter, text)
        print(f"   {letter}) is counted {count} times in your string")
    

if __name__ == "__main__":
    main()
