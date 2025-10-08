length = float(input("length of person [m]: "))
weight = float(input("weight of person [kg]: "))

Bmi = weight/ (length * length)
melding = ""

if Bmi < 18.5:
    melding = "Ondergewicht"
    
elif 18.5 < Bmi < 25:
    melding = "Gezond gewicht"

elif 25 < Bmi < 30:
    melding = "Over gewicht"

else :
    melding = "Obesitas"
    
print(f"BMI of person is: {Bmi}, dat is in de categorie: {melding}")