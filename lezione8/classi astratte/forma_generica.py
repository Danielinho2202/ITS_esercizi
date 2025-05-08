from abc import ABC, abstractmethod

class Forma_generica(ABC):
    
    @abstractmethod
    def draw(self) -> None:
        pass

    def setShape(self,shape) -> None:
        if shape:
            self.shape=shape
        else:
            print ("Errore")
    def getShape(self) -> str:
        return self.shape