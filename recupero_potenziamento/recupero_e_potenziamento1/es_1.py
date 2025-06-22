def calculateCharges(car:str,h:float) ->float:
    totale=0
    ore_usate=0
    if h==24:
        totale=10
        return f"{car:<10} {h:<10} {totale:<10}"
    elif h<=3:
        totale=2
        return f"{car:<10} {h:<10} {totale:<10}"
    else:
        ore_usate=3
        totale=2
        while h>ore_usate:
            ore_usate+=1
            totale+=0.50
        return f"{car:<10} {h:<10} {totale:<10}"
    
c1=calculateCharges("car1",1.5)
c2=calculateCharges("car2",4.0)
c3=calculateCharges("car3",24)
c4=calculateCharges("car4",6.5)

print(c1)
print(c2)
print(c3)
print(c4)

