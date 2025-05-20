class Persona:
    def __init__(self):
        self.name= ""
        self.lastname=""
        self.age=0


    def displayData(self) -> None:
        print (f"Nome: {self.name}\nCognome: {self.lastname}\netà: {self.age}")

    #funzione che mi consente di impostare il valore di self.name
    def setname(self,name:str) -> None:
        self.name = name

    def setlastname(self, lastname:str):
        self.lastname =lastname

    def setage(self, age:int):
        if age<0 or age>130:
            self.age=0
        else:
            self.age=age

    #fuznione per tornare il valotre di slef.name

    def getname(self) -> str:
        return self.name
    def getlastname(self) -> str:
        return self.lastname
    def getage(self)  -> int:
        return self.age






