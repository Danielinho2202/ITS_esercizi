'''Scrivere un programma che consenta all'utente di inserire una sequenza 
di numeri reali non negativi (sia interi che decimali). L'inserimento 
termina quando viene fornito un numero negativo, che funge da sentinella 
e non deve essere considerato nei calcoli.

Il programma deve:

    Calcolare la media dei soli numeri interi inseriti. 
    Utilizzate la funzione is_integer() per verificare se 
    il numero inserito è un intero.
    Determinare e visualizzare il numero più grande e il numero 
    più piccolo tra tutti quelli inseriti (sia interi che decimali).'''


numero=(float(input("inserisci un numero")))
numero_max=numero
numero_min=numero
i=0                                         #inizializziamo i valori
somma=0                                         
while numero>=0:
        if numero.is_integer():             #verifichiamo se è intero
            somma= somma+numero
            i+=1
        if numero>numero_max:
            numero_max= numero
        elif numero < numero_min:            #verifichiamo se è valore massimo o minimo
            numero_min= numero
        numero=(float(input("inserisci un numero")))

if i>0:                             #verifica se sono stati inseriti valori interi
     media= somma/i
     print (media)
else:
     print ("non ci sono numeri interi per fare la media")
print (numero_max)
print (numero_min)



        
            
        



