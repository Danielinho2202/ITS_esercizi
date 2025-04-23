from persona import Persona

class Studente(Persona):
    def __init__(self, name: str, lastname: str, age: int, matricola: str):
        super().__init__(name, lastname, age)
        self.setMatricola(matricola)

    def setMatricola(self, matricola: str):
        if matricola:
            self.matricola = matricola
        else:
            print("Errore, no stringa vuota")

    def getMatricola(self):
        return self.matricola

    def __str__(self):
        #per richiamare l'str della classe persona, vanno bene entrambi
        return f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}\nMatricola: {self.getMatricola()}"
    
    def get_media_esami(self, voti_esami:list):
        if voti_esami:
            somma=0
            for voto in voti_esami:
                somma += voti_esami
            return round(somma/len(voti_esami),2)
        else:
            return 0.00
        
    #metodo che consente di stabilire se questi 2 oggetti sono uguali
    def __eq__(self, other) -> bool:
        if other is None or not isinstance (other,type(self)):
            return False
        else:
            return self.getMatricola()== other.getMatricola()
        

  
