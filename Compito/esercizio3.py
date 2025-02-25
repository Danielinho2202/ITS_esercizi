'''Scrivere un programma che acquisisca una stringa 
inserita dall'utente e generi una nuova stringa che 
corrisponda alla versione invertita della stringa originale. 
Il programma deve poi visualizzare la stringa ottenuta in output. 
Per risolvere il problema non si deve utilizzare alcun tipo di 
funzione, ma esclusivamente i cicli.'''

stringa=(str(input("inserisci una parola")))
stringa_al_contrario=""             #inizializziamo la stringa da riempire

for i in range (len(stringa)-1,-1,-1):
    stringa_al_contrario= (stringa_al_contrario) + stringa[i]
print (stringa_al_contrario)


