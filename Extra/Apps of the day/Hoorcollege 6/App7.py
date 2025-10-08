text = input("Give string: ")

letters = []

for i in text:
    letters.append(ord(i))

letters.sort()
print(letters)

for i in letters:
    print(chr(i), end='')
