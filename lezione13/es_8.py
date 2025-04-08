'''Si scriva una funzione ricorsiva vowelsCounter che conti il numero di vocali in una stringa.

Suggerimento: ogni volta che si effettua una chiamata ricorsiva, si utilizzi lo slicing per 
ottenere una nuova stringa formata dai caratteri compresi tra il secondo e l'ultimo della stringa originale.
L'ultima chiamata ricorsiva avverrà quando la stringa non contiene caratteri.'''


def vowelsCounter(stringa:str):
    if stringa=="":
        return 0
    if stringa[0]=="a" or stringa[0]=="e" or stringa[0]=="i" or stringa[0]=="o" or stringa[0]=="u":
        return 1 + vowelsCounter(stringa[1:])
    else:
        return (vowelsCounter(stringa[1:]))
    
print (vowelsCounter("ciao"))