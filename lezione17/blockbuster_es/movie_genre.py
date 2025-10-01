from film import Film

class Azione(Film):

    def __init__(self, id, titolo):
        super().__init__(id, titolo)
        self.genere:str="Azione"
        self.penale:int=3

    def getGenere(self):
        return self.genere
    
    def getPenale(self):
        return self.penale
    
    def calcolaPenaleRitardo(self,giorni):
        return giorni*self.getPenale()
        

class Commedia(Film):

    def __init__(self, id, titolo):
        super().__init__(id, titolo)
        self.genere:str="Commedia"
        self.penale:float=2.50

    def getGenere(self):
        return self.genere
    
    def getPenale(self):
        return self.penale
    
    def calcolaPenaleRitardo(self,giorni):
        return giorni*self.getPenale()

class Drama(Film):
    def __init__(self, id, titolo):
        super().__init__(id, titolo)
        self.genere:str="Drama"
        self.penale:int=2

    def getGenere(self):
        return self.genere
    
    def getPenale(self):
        return self.penale
    
    def calcolaPenaleRitardo(self,giorni):
        return giorni*self.getPenale()