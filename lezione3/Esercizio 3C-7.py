'''Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce 
"c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".

NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.'''

print ('Per ciascun lancio della moneta inserisci "t" o "T" se è uscito "testa" mentre inserisci "c" o "C" se è uscito "croce".')

counter_c=0
counter_t=0


i=1
while i < 9:
    lancio=str(input(f"Lancio {i}: "))
    match lancio:
        case "c"|"C":
            counter_c+=1
            i+=1
        case "T"|"t":
            counter_t+=1
            i+=1
        case _: 
            print ("lancio non valido")

percentuale_c= counter_c/8*100
percentuale_t= counter_t/8*100


print (f"totale testa= {counter_t}")
print (f"totale croce= {counter_c}")
print (f"percentuale testa= {percentuale_t:.2f}%")
print (f"percentuale croce= {percentuale_c:.2f}%")


