class Alieno:

    '''galassia di provenienza'''
    def __init__(self,galaxy: str):
        self.setGalaxy(galaxy)

    def setGalaxy(self, galaxy) -> None:
        if galaxy:
            self.galaxy=galaxy
        else:
            print ("Errore, non deve essere vuota!")
    def getGalaxy(self)-> str:
        return self.galaxy
    def __str__ (self) -> str:
        return f"\nAlieno dalla galassia {self.getGalaxy()}\n"
    def speak(self) -> None:
        print ("ibvrfdusuvuy")