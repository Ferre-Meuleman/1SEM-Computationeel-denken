conversion = int(input("Choose your conversion:\n   1) C to F\n   2) F to C \n"))

if conversion == 1:
    cel = float(input("Give your themperature in Celsius: "))
    fah = (5/9) * cel + 32
    print(f"Your celsius to fahrneheit is {cel}C --> {fah:0.2f}F")
    
elif conversion == 2:
    fah = float(input("Give your themperature in Celsius: "))
    cel = (5/9) * (fah - 32)
    print(f"Your fahrneheit to celsiusis {fah}F --> {cel:0.2f}C")
    
else:
    print("No nown conversion")