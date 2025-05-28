class Libro:
    def __init__(self, titolo: str, autore: str, disponibile: bool = True):
        self.titolo = titolo
        self.autore = autore
        self.disponibile = disponibile 
    def crea_libro(self,titolo,autore,disponibile):
        libro:dict={ "titolo": titolo,
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
            print (f"libro : {titolo} aggiunto")

        return (self.libreria)
    def presta_libro(self,titolo_prestito):
        for libro in self.libreria:
            if titolo_prestito==libro["titolo"] and libro["disponibile"]==False:
                print ("libro già prestato")
                return
            if titolo_prestito==libro["titolo"] and libro["disponibile"]==True:
                print(f"libro {titolo_prestito} prestato")
                libro["disponibile"]=False
                return
        print ("libro non trovato")

    def restituisci_libro(self,titolo_restituito):
        for libro in self.libreria:
            if titolo_restituito==libro["titolo"] and libro["disponibile"]==True:
                print ("libro non è stato prestato o e già stato restituito")
                return
            elif titolo_restituito==libro["titolo"] and libro["disponibile"]==False:
                libro["disponibile"]=True
                print (f"libro {titolo_restituito} restituito")
                return
        print ("libro non esistente")
            
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

b.restituisci_libro("1984")
b.restituisci_libro("1984")
b.restituisci_libro("a")

print(b.mostra_libri())




        

        


