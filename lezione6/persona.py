class Persona:
    #costruttore
    def __init__(self, name:str, lastname:str, age:int):
        self.name=name
        self.lastname= lastname
        self.age= age

#funzione che mostra in output i dati relativi ad una persona
    def displayData(self) -> None:
        print (f"Nome: {self.name}\nCognome: {self.lastname}\netà: {self.age}")
        
