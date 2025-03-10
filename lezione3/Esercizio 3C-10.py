'''Scrivere un programma in Python che permetta all'utente di inserire una data 
(giorno e mese espressi in forma numerica), salvi la data in una tupla e utilizzi 
un match statement per verificare se la data corrisponde a una festività o a un evento speciale:

- Capodanno → 1 Gennaio → "Capodanno"
- San Valentino → 14 Febbraio → "San Valentino"
- Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
- Ferragosto → 15 Agosto → "Ferragosto"
- Halloween → 31 Ottobre → "Halloween"
- Natale → 25 Dicembre → "Natale"
- Altro caso → "Nessuna festività importante in questa data."
'''



giorno=int(input("inserisci giorno: "))
mese=int(input("inserisci mese: "))
data=False

while data!=True:
    match mese:
        case 2:
            match giorno:
                case giorno if giorno>28:
                    print ("data non esistente")
                    giorno=int(input("inserisci giorno: "))
                    mese=int(input("inserisci mese: "))
                case _:
                    data=True
        case 4|6|9|11:
            match giorno:
                case giorno if giorno>30:
                    print ("data non esistente")
                    giorno=int(input("inserisci giorno: "))
                    mese=int(input("inserisci mese: "))
                case _:
                    data=True
        case mese if mese<13:
            match giorno:
                case giorno if giorno>31:
                    print ("data non esistente")
                    giorno=int(input("inserisci giorno: "))
                    mese=int(input("inserisci mese: "))
                case _:
                    data=True
        case _:
            print ("data non esistente")
            giorno=int(input("inserisci giorno: "))
            mese=int(input("inserisci mese: "))

      

data=(giorno, mese)

match data:
    case (1,1):
        print (f"Il {giorno}/{mese} è Capodanno!")
    case (14,2):
        print (f"Il {giorno}/{mese} è San Valentino!")
    case (giorno, 6):
        print (f"Il {giorno}/{mese} è Festa della Repubblica Italiana!")
    case (15, 8):
        print (f"Il {giorno}/{mese} è Ferragosto!")
    case (31, 10):
        print (f"Il {giorno}/{mese} è Halloween!")
    case (25, 12):
        print (f"Il {giorno}/{mese} è Natale!")
    case _:
        print (f"Il {giorno}/{mese} non c'è nessuna festività importante")



