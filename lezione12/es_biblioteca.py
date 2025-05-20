class Libro:
    def __init__(self, titolo: str, autore: str, disponibile: bool = True):
        self.titolo = titolo
        self.autore = autore
        self.disponibile = disponibile 
    def crea_libro(self,titolo,autore,disponibile):
        libro:Libro={ "titolo": titolo,
        "autore": autore,
        "disponibile": disponibile}
        return libro

class Biblioteca:
    def __init__(self):
        self.libreria = []
        self.check_libro=True

    def aggiungi_libro(self, titolo, autore, disponibile=True):
        nuovo_libro = Libro.crea_libro(self,titolo, autore, disponibile)
        for libro in self.libreria:
            if nuovo_libro["titolo"]== libro["titolo"]:
                print("errore")
                self.check_libro=False
        if self.check_libro==True:
            self.libreria.append(nuovo_libro)

        return (self.libreria)
    def presta_libro(self,titolo_prestito):
        for libro in self.libreria:
            if titolo_prestito==libro["titolo"] and libro["disponibile"]==False:
                print ("libro già prestato")
                return
            if titolo_prestito==libro["titolo"] and libro["disponibile"]==True:
                print("prestito effettuato")
                libro["disponibile"]=False
                return
        print ("libro non trovato")
            
    def mostra_libri(self):
        return self.libreria
        
            



b = Biblioteca()
b.aggiungi_libro("1984", "George Orwell")
b.aggiungi_libro("Brave New World", "Aldous Huxley")
b.aggiungi_libro("b","b")

b.presta_libro("1984")  # Prestato con successo
b.presta_libro("1984")  # Già prestato
b.presta_libro("Il nome della rosa")  # Libro non trovato
b.presta_libro("b")

print(b.mostra_libri())




        

        


