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

    def aggiungi_libro(self, titolo, autore, disponibile=True):
        nuovo_libro = Libro.crea_libro(self,titolo, autore, disponibile)
        if nuovo_libro["titolo"]==self.libreria[titolo]:
            self.libreria.append(nuovo_libro)

        print (self.libreria)


b=Biblioteca()
b = Biblioteca()
print(b.aggiungi_libro("1984", "George Orwell"))  
print(b.aggiungi_libro("1984", "George Orwell"))




        

        


