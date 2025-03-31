import random
#creiamo il percorso

def visualizza (posizione_tartaruga,posizione_lepre):
    percorso=[]
    i=0
    while i in range (70):
        percorso.append("_")
        i+=1

    ostacoli:dict={15:-7,30:-3,45:-7,60:-3}
    bonus:dict={10:3,25:6,40:10,55:3}


    if posizione_tartaruga==posizione_lepre:
        percorso[posizione_tartaruga]= "ouch!"
    else:
        percorso[posizione_tartaruga]="T"
        percorso[posizione_lepre]="L"
    
    print("".join(percorso))

def meteo_(n):
    if (n//10)%2==0:
        return "sole"
    else:
        return "pioggia"


def tartaruga(posizione,meteo,energia):
    dado=random.randint(1,10)
    ostacoli:dict={15:-7,30:-3,45:-7,60:-3}
    bonus:dict={10:3,25:6,40:10,55:3}
    if 1<=dado<=5:
        if energia>=5:
            energia-=5
            posizione+=3
        else:
            energia = min(energia + 10, 100)   
    elif 6<=dado<=7:
        if energia>=10:
            energia-=10
            posizione-=6
        else:
            energia = min(energia + 10, 100)
    else:
        if energia>=3:
            energia-=3
            posizione+=1
        else:
            energia = min(energia + 10, 100)
    if meteo=="pioggia":
        posizione-=2

    if posizione in ostacoli.keys():
        posizione=posizione + ostacoli[posizione]
    if posizione in bonus.keys():
        posizione= posizione + bonus[posizione]
        


    if posizione<=0:
        posizione=0

    return posizione,energia
    


def lepre(posizione,meteo,energia):
    dado=random.randint(1,10)
    ostacoli:dict={15:-7,30:-3,45:-7,60:-3}
    bonus:dict={10:3,25:6,40:10,55:3}
    if 1<=dado<=2:
        energia = min(energia + 10, 100)
    elif 3<=dado<=4:
        if energia>=15:
            energia-=15
            posizione+=9
        else:
            pass
    elif dado==5:
        if energia>=20:
            energia-=20
            posizione-=12
        else:
            pass
    elif 6<=dado<=8:
        if energia>=5:
            energia-=5
            posizione+=1
        else:
            pass
    else:
        if energia>=8:
            energia-=8
            posizione-=2
        else:
            pass
    if meteo=="pioggia":
        posizione-=2
    
    if posizione in ostacoli.keys():
        posizione=posizione + ostacoli[posizione]
    if posizione in bonus.keys():
        posizione= posizione + bonus[posizione]
        
    
    if posizione<0:
        posizione=0

    return posizione,energia




def gara():
    print ("Partenza!")
    posizione_tartaruga=0
    posizione_lepre=0
    energia_tartaruga=100
    energia_lepre=100
    n=0
    

    while True:
        meteo=meteo_(n)
        n+=1
        
       
        posizione_tartaruga,energia_tartaruga=tartaruga(posizione_tartaruga,meteo,energia_tartaruga)
        posizione_lepre,energia_lepre=lepre(posizione_lepre,meteo,energia_lepre)
        
        

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

    








