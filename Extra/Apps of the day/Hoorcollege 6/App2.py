number = int(input("Give a number: "))

def GreroryLeibnitz(num: int):
    i = 1
    x = 1
    tussen = 0
    
    while i <= num:
        tussen += (-1 if i%2 == 0 else 1) * 1/x
        x +=2
        i +=1
    
    pi = 4* tussen
    
    return pi
        
print(GreroryLeibnitz(number))