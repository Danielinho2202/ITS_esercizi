'''Si scriva una funzione ricorsiva charDuplicator che consenta di duplicare ogni carattere in una 
stringa e restituisca il risultato sotto forma di una nuova stringa.

Ad esempio, se la stringa "libro" viene data in input a charDuplicator, la funzione 
ricorsiva deve produrre in output la stringa "lliibbrroo".'''

def charDuplicator(stringa:str):
    if stringa=="":
        return ""
    else:
        return stringa[0]+stringa[0]+charDuplicator(stringa[1:])

print (charDuplicator("ciao"))
