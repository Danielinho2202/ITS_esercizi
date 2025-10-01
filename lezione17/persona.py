class Persona:
    _nome:str
    _cognome:str
    _eta:int

    def __init__(self,fn,ln):
        if isinstance (fn,str) and isinstance (ln,str):
            self.fn=fn
            self.ln=ln
        elif isinstance (fn,str) or isinstance (ln,str):
            if isinstance (fn,str):
                self.fn=fn
            if isinstance (ln,str):
                self.ln=ln
        

    def setName(self,fn):
        