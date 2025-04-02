'''<Scrivere in Python una funzione recursivePower che calcola la potenza di un numero utilizzando la ricorsione. 
La funzione deve ricevere due parametri in input:
base: il numero da elevare a potenza.
exponent: l’esponente a cui elevare la base.

Utilizzare, poi, la funzione per calcolare:

    3⁴, ovvero 3 elevato alla potenza di 4. 
    43 , ovvero 4 elevato alla potenza di 3.
    25, ovvero 2 elevato alla potenza di 5. 
    52, ovvero 5 elevato alla potenza di 2.
'''

def recursivePower(base:int,esponente:int):
    if esponente==0:
        base=1
        return base
    elif esponente ==1:
        return base
    else:
        return (base*recursivePower(base,esponente-1))
    
print (recursivePower(3,4))
print (recursivePower(4,3))
print (recursivePower(9,1))
print (recursivePower(8,0))

    

    
