number = int(input("Give a number: "))

def MultiplicationTable(num: int):

    i = 1
    while i <= 10:
        product = i * num
        print(f"{i} * {num} = {product}")
        i +=1
        
MultiplicationTable(number)