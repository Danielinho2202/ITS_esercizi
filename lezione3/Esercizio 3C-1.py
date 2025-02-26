'''Scrivere un programma in Python che utilizzi un match statement per classificare un 
voto scolastico in base alla scala italiana.
Il programma deve accettare in input un voto numerico intero da 1 a 10 e stampare la 
valutazione corrispondente:

- 10 → "Eccellente"
- 8-9 → "Molto buono"
- 6-7 → "Sufficiente"
- 4-5 → "Insufficiente"
- 1-3 → "Gravemente insufficiente"
- Altro caso → "Voto non valido"'''


voto=int(input("inserisci il voto: "))

match voto:
    case 10:
        print ("Eccellente")
    case 8|9:
        print ("molto buono")
    case 6|7:
        print ("Sufficiente")
    case 4|5:
        print ("Insufficente")
    case 1|2|3:
        print ("Gravemente insufficiente")
    case _:
        print ("Voto non valido")
