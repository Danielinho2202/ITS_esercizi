'''l valore di π può essere approssimato utilizzando la seguente serie infinita:

π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

Scrivere un programma che calcoli il valore di π utilizzando questa serie e determini 
quanti termini sono necessari per ottenere approssimazioni sempre più accurate. Quindi:

    progettare un algoritmo che mostri in output quanti termini della serie devono
    essere usati per ottenere il valore di π ≈ 3.14;
    modificare l'algoritmo, mostrando in output quanti termini della serie devono 
    essere usati per ottenere il valore di π ≈ 3.141;
    modificare l'algoritmo, mostrando in output quanti termini della serie devono
    essere usati per ottenere il valore di π ≈ 3.1415;
    modificare l'algoritmo, mostrando in output quanti termini della serie devono 
    essere usati per ottenere il valore di π ≈ 3.14159.

Nota: Il programma deve iterare fino a raggiungere ciascuna delle soglie indicate, contando il numero di termini necessari.
'''

denominatore:int = 1 
totale:float = 4.0
count:int = 0

while round(totale, 2) != 3.14:
    
    if count%2!=0:                                      
        totale = totale - 4/denominatore
    else:
        totale = totale + 4/denominatore
    
    
    count+=1
    denominatore+=2
print(count)



        
