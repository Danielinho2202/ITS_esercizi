denominatore: int = 1
totale:float = 0.0
count:int = 0
segno = 1
while round(totale, 2) != 3.14:
    totale += segno * (4/denominatore)

    """    if count%2==0:
        totale = totale + 4/denominatore
    else:
        totale = totale - 4/denominatore"""
    segno *= -1
    count += 1
    denominatore += 2
    print(totale)

print(count)