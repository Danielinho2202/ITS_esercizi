'''Si scriva una funzione ricorsiva vowelRemover che elimini tutte le vocali da una stringa data e 
restituisca sotto forma di una nuova stringa la stringa originale ma senza le vocali.

Suggerimento: utilizzare l'operatore + per realizzare la concatenazione di stringhe al fine di costruire 
la stringa da restituire.'''

def vowelRemover(stringa:str):
    if stringa=="":
        return ""
    if stringa[0]=="a" or stringa[0]=="e" or stringa[0]=="i" or stringa[0]=="o" or stringa[0]=="u":
        return vowelRemover(stringa[1:])
    else:
        return stringa[0]+vowelRemover(stringa[1:])
    
print (vowelRemover("ciao"))
    