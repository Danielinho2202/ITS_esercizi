'''Scrivere un programma in Python che chieda all'utente di inserire il proprio nome 
e il proprio genere (specificato con "m" per maschio o "f" per femmina) e utilizzi lo 
statement match per fornire una risposta adeguata da inserire in un documento di identita'.

- Se il valore di gender è "m", stampare il nome e il genere come Maschio.
- Se il valore di gender è "f", stampare il nome e il genere come Femmina.
- Se il valore di gender è diverso da "m" o "f", stampare un messaggio di errore, indicando 
che non è possibile generare un documento di identità.'''

nome=(str(input("Inserire nome: ")))
gender=(str(input("Inserire gender. Digitare m per maschio e f per femmina: ")))

print (f"Nome: {nome}")

match gender:
    case "m":
        print ("Gender: Maschio")
    case "f":
        print ("Gender: Femmina")
    case _:
        print (f"Mi dispiace {nome}, non e' possibile procedere con la generazione di un documento di identità!")

