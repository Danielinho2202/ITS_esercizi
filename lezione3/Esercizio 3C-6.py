'''Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere un codice python che 
consenta all'utente di inserire il nome di un animale ed un habitat. Quando il codice dell'esercizo
 3C-4 classifica l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci, 
 oltre a mostrare un messaggio a schermo, deve salvare tale categoria in una variabile animal_type. 
 Se l'animale inserito non è classificabile in una delle quattro categorie proposte, il valore di 
 animal_type sarà ' "unknown".

Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type)
 e l'habitat.

Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere 
nell'habitat inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.'''

Mammiferi=["cane","gatto","cavallo","elefante","leone","balena","delfino"]
Rettili=["serpente","lucertola","tartaruga","coccodrillo"]
Uccelli=["aquila","pappagallo","gufo","falco","cigno","anatra","gallina","tacchino"]
pesci=["squalo","trota","salmone","carpa"]
habitat_type=["terra","acqua","aria"]

animale=str(input("Inserisci un animale: ")).lower()

match animale:
    case animale if animale in Mammiferi:
        print (f"{animale} appartiene alla categoria dei mammiferi!")
        animal_type="mammiferi"
    case animale if animale in Rettili:
        print (f"{animale} appartiene alla categoria dei rettili!")
        animal_type="rettili"
    case animale if animale in Uccelli:
        print (f"{animale} appartiene alla categoria degli uccelli!")
        animal_type="uccelli"
    case animale if animale in pesci:
        print (f"{animale} appartiene alla categoria dei pesci!")
        animal_type="pesci"
    case _: 
        (f"Non so a che categoria appartiene {animale}!")
        animal_type="sconosciuto"

habitat=str(input("Inserisci l'habitat in cui vive l'animale: ")).lower()

info_animale={"nome":animale,"categoria":animal_type,"habitat":habitat}

match info_animale:
    case info_animale if "categoria"=="mammiferi" :
        match animale:
            case "balena"|"delfino":
                if habitat=="acqua":
                    print (f"L'animale {animale} è uno dei mammiferi che può vivere in {habitat}!")
                else:
                    print (f"non ho mai visto l'animale {animale} vivere nell'habitat {habitat}")
            case _:
                if habitat=="terra":
                    print (f"L'animale {animale} è uno dei mammiferi che può vivere in {habitat}!")
                else:
                    print (f"non ho mai visto l'animale {animale} vivere nell'habitat {habitat}")
    case info_animale if "categoria"=="rettili":
        match animale:
            case "coccodrillo"|"tartaruga":
                if habitat=="terra" or habitat=="acqua":
                    print (f"L'animale {animale} è uno dei mammiferi che può vivere in {habitat}!")
                else:
                    print (f"non ho mai visto l'animale {animale} vivere nell'habitat {habitat}")
            










