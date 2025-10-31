user_input = int(input("Give number of rows for the three: "))
maxchar = user_input*2 + 1
for i in range(0, user_input):
    stars = i*2 + 1

    white_spaces = int((maxchar - stars)/2)
    string = ""

    for j in range(0, white_spaces):
        string += " "

    for x in range(0, stars):
        string += "*"

    for y in range(0, white_spaces):
        string += " "
    print(string)
