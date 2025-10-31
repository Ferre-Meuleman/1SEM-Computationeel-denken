import datetime

Day =   int(input("Give a number to represet the day: "))
Month = int(input("Give a number to represet the month: "))
Year =  int(input("Give a number to represet the year: "))

maxdate = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if Year % 4 == 0:
        maxdate[1] += 1

if (Month <= 12) and (Day <= maxdate[Month-1]) :
    print(f"The date {Day}/{Month}/{Year} does exist")

else:       
    print(f"The date {Day}/{Month}/{Year} does not exist")

"""
oplossing met functies

try:
    datetime.datetime(year=Year,month=Month,day=Day)
    print(f"The date {Day}/{Month}/{Year} does exist")
except ValueError:
    print(f"The date {Day}/{Month}/{Year} does not exist")
"""