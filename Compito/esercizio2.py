'''Scrivere un programma che acquisisca una stringa inserita 
dall'utente e calcoli il numero totale di spazi presenti nella 
stringa. Il risultato deve essere visualizzato in output.'''

frase=(str(input("inserisci una frase")))
count=0
for carattere in frase:
    if carattere == " ":
        count = count+1 
    
print (f"Nella frase ci sono {count} spazi.")