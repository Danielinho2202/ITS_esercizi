'''crivere un programma in Python che converta un voto di laurea italiano 
(sistema in 110-emi) nel sistema GPA americano (scala 0-4).
Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, 
espresso come numero intero e usare un match per determinare il corrispondente 
GPA americano, secondo questa tabella di conversione:

- 106-110 → 4.0
- 101-105 → 3.7
- 96-100 → 3.3
- 91-95 → 3.0
- 86-90 → 2.7
- 81-85 → 2.3
- 76-80 → 2.0
- 70-75 → 1.7
- 66-69 → 1.0
- Altro caso → "Voto non valido"
'''

v=int(input("inserisci il voto di laurea: "))

match v:
    case v if v<111 and v>105:
        print ("GPA= 4.0")
    case v if v<106 and v>100:
        print ("GPA= 3.7")
    case v if v<101 and v>95:
        print ("GPA= 3.3")
    case v if v<96 and v>90:
        print ("GPA= 3.0")
    case v if v<91 and v>85:
        print ("GPA= 2.7")
    case v if v<86 and v>80:
        print ("GPA= 2.3")
    case v if v<81 and v>75:
        print ("GPA= 2.0")
    case v if v<76 and v>69:
        print ("GPA= 1.7")
    case v if v<70 and v>65:
        print ("GPA= 1.0")
    case _:
        print ("Voto non valido")
