WorkedHours = int(input("Give worked hours: "))

if WorkedHours <= 38:
    print(f"No overhours just worked {WorkedHours}")
    
elif 38 < WorkedHours <= 60:
    Overhours = WorkedHours - 38
    print(f"Worked: \n Overhours: {Overhours}")

else:
    Overhours = WorkedHours - 60
    print(f"Worked: \n Hours: 38 \n Overhours: 22 \n Dubblehours: {Overhours}")