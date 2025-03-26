import random
#creiamo il percorso

def visualizza (posizione_tartaruga,posizione_lepre):
    percorso=[]
    i=0
    while i in range (70):
        percorso.append("_")
        i+=1

    if posizione_tartaruga==posizione_lepre:
        percorso[posizione_tartaruga]= "ouch!"
    else:
        percorso[posizione_tartaruga]="T"
        percorso[posizione_lepre]="L"
    
    print("".join(percorso))


    

def tartaruga(posizione):
    dado=random.randint(1,10)
    if 1<=dado<=5:
        posizione+=3
    elif 6<=dado<=7:
        posizione-=6
    else:
        posizione+=1
    if posizione<=0:
        posizione=0


    return posizione


def lepre(posizione):
    dado=random.randint(1,10)
    if 1<=dado<=2:
        pass
    elif 3<=dado<=4:
        posizione+=9
    elif dado==5:
        posizione-=12
    elif 6<=dado<=8:
        posizione+=1
    else:
        posizione-=2
    if posizione<0:
        posizione=0

    return posizione




def gara():
    print ("Partenza!")
    posizione_tartaruga=0
    posizione_lepre=0
    while True:
        
        posizione_tartaruga=tartaruga(posizione_tartaruga)
        posizione_lepre=lepre(posizione_lepre)

        if posizione_tartaruga>69 and posizione_lepre>69:
            print ("pareggio")
            break
        elif posizione_lepre>69:
            print ("la lepre vince")
            break
        elif posizione_tartaruga>69:
            print ("la tartaruga vince")
            break

        

        visualizza(posizione_tartaruga,posizione_lepre)




gara()

    








