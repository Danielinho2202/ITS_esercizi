class Film:
    id:int
    titolo:str

    def __init__(self,id,titolo):
        self.setId(id) 
        self.setTitolo(titolo)

    def setId(self,id):
        if self.id:
            self.id=id
        

    def setTitolo(self,titolo):
        if self.titolo:
            self.titolo=titolo

    def getId(self):
        return self.id
    
    def getTitolo(self):
        return self.titolo
    
    def isEqual(self,other):
        return self.getId() == other
    

