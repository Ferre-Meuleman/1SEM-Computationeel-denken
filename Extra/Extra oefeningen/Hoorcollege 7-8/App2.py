"""Gegeven  is  een  array  die  bestaat  uit  N  elementen  waarbij  elk  element  een  getal  bevat  van  1  t.e.m.  N  Schrijf  een 
programma om te detecteren of er duplicaten voorkomen."""

givven_array = [1, 2, 3, 4, 5, 3]

for i in range(len(givven_array)):
    for j in range(i + 1, len(givven_array)):
        if givven_array[i] == givven_array[j]:
            print("Duplicaat gevonden:", givven_array[i])
            break
    else:
        continue
    break