def word_count(text: str):
    text = text.lower()  # case-insensitive
    words = []
    current_word = ""

    for char in text:
        if char.isalpha():
            current_word += char
        else:
            if current_word != "":
                words.append(current_word)
                current_word = ""
                
    if current_word != "":
        words.append(current_word)

    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    for word in sorted(counts.keys()):
        print(f"{word}: {counts[word]}")

def main():
    text = input("Voer een tekst in: ")
    word_count(text)

if __name__ == "__main__":
    main()
