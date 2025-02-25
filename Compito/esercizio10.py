'''Scrivere un programma che permetta di analizzare una lista di numeri interi 
inseriti dall’utente.

Il programma deve:

    acquisire una sequenza di numeri interi, terminando l’inserimento quando 
    l’utente digita 0 (che non deve essere considerato nei calcoli);
    calcolare e visualizzare la somma di tutti i numeri pari inseriti;
    calcolare e visualizzare la media di tutti i numeri dispari inseriti;
    determinare e visualizzare il numero con la frequenza più alta (cioè quello 
    che compare più volte nella lista);
    se più numeri hanno la stessa frequenza massima, visualizzarli tutti.
'''

n=(int(input("inserisci un numero: ")))
somma_pari=0
somma_dispari=0
count_dispari=0
frequenza={}
while n!=0:
    if n%2==0:
        somma_pari=somma_pari+n
    else:
        somma_dispari=somma_dispari+n
        count_dispari+=1
    if n in frequenza:                          #verifichiamo se il numero è nuovo nel dizionario; se si aggiungiamo una nuova chiave con il numero,
                                                #altrimenti aggiorniamo il valore della frequenza.
        frequenza[n]+=1
    else:
        frequenza[n]=1
    n=(int(input("inserisci un numero: ")))

max_frequenza=(max(frequenza.values()))
numeri_frequenti = [num for num, freq in frequenza.items() if freq == max_frequenza]       
#qui iteriamo ogni numero e sua frequenza, e verifichiamo se è uguale alla max_frequenza 
# che abbiamo identifivato prima (ho trovato spunto da internet, spero vada bene).



print (f"la somma dei numeri pari è: {somma_pari}")
print (f"la media dei numeri dispari è:{somma_dispari/count_dispari}")
print (f"i numeri con frequenza più alta, di frequenza {max_frequenza} sono: {numeri_frequenti}.")