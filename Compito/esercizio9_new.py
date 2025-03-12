denominatore: int = 1
totale:float = 4.0
count:int = 0

while round(totale, 2) != 3.14:
    if count%2==0:
        totale = totale + 4/denominatore
    else:
        totale = totale - 4/denominatore
    
    count += 1
    denominatore += 2

print(count)