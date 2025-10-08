for i in range(26):
    print(chr(ord('A') + i), end='')

print()

for i in range(26):
    letter = chr((ord('A') + i - ord('A') + 13) % 26 + ord('A'))
    print(letter, end='')
