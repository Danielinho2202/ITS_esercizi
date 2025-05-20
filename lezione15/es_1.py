class FileManager:
    def __init__(self,nome,mode,coding):
        self.nome=nome
        self.mode=mode
        self.coding=coding
 
    def __enter__(self):
        self.file=open(self.nome,self.mode,encoding=self.coding)
        print ("Risorsa ricevuta")
        return self.file

    def __exit__(self,exc_type,exc_value,traceback):
        print ("Risorsa rilasciata")
        if exc_type is not None:
            print (f"Errore: {exc_type},{exc_value},{traceback}")
        return False
    

with FileManager("lezione15/example.txt","w","utf-8") as file:
    file.write("Hello world")