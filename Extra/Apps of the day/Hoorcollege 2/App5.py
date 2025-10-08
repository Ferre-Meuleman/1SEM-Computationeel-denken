beers = int(input("Give a number of beers: "))

while beers != 0:
    if beers == 2:
        print(f"{beers} flesjes met bier op de muur, {beers} flesjes met bier. Open er een, drink hem meteen, {beers - 1} flesje met bier op de muur.")
    
    elif beers == 1:
        print(f"{beers} flesje met bier op de muur, {beers} flesje met bier. Open er een, drink hem meteen, geen flesjes met bier op de muur.")    
    
    else:
        print(f"{beers} flesjes met bier op de muur, {beers} flesjes met bier. Open er een, drink hem meteen, {beers - 1} flesjes met bier op de muur.")
    beers -= 1
