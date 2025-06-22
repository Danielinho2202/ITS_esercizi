from __future__ import annotations
from random import *
class Creatura:
    __nome:str


    def set_Nome(self,__nome):
        if not isinstance(__nome,str):
            __nome="Creatura Generica"
            print ("Deve essere una stringa")
        self.__nome=__nome

    def __init__(self,__nome):
        self.set_Nome(__nome)

    def get_nome(self):
        return self.__nome
    
    def __str__(self):
        return f"Creatura: {self.get_nome()}"
    
class Alieno(Creatura):
    __matricola:str
    __munizioni:list

    def __set_matricola(self):
        self.__matricola=str(randint(10000,90000))

    def get_matricola(self):
        return self.__matricola
    
    def __set_munizioni(self):
        self.__munizioni=[]
        for n in range (15):
            self.__munizioni.append(n**2)

    def get_munizioni(self):
        return self.__munizioni

    def __init__(self,__nome):
        self.__set_munizioni()
        self.__set_matricola()
        if __nome != "Robot":
            print ("""Attenzione! Tutti gli Alieni 
                    devono avere il nome "Robot" seguito dal numero 
                   di matricola! Reimpostazione nome Alieno in Corso!""")
        self.set_Nome("Robot"+"-"+self.get_matricola())

    def __str__(self):
        return f"Alieno: {self.get_nome()}"



class Mostro(Creatura):
    vittoria:str
    sconfitta:str
    assalto:list[int]


    def __init__(self, __nome,vittoria:str,sconfitta:str):
        super().__init__(__nome)
        self.__set_vittoria(vittoria)
        self.__set_sconfitta(sconfitta)
        self.__set_assalto()
        

    def __set_assalto(self):
        self.assalto=[]
        for i in range(1,16):
            n=randint(1,100)
            while n in self.assalto:
                n=randint(1,100)
            self.assalto.append(n)

    def get_assalto(self):
        return self.assalto


    def __set_vittoria(self,vittoria:str):
        if not isinstance (vittoria,str):
            self.vittoria="GRAAAHHH"
        else:
            self.vittoria=vittoria

    def get_vittoria(self):
        return self.vittoria

    def __set_sconfitta(self,sconfitta:str):
        if not isinstance (sconfitta,str):
            self.sconfitta="Uuurghhh"
        else:
            self.sconfitta=sconfitta
    def get_sconfitta(self):
        return self.sconfitta

    def __str__(self):
        nome_vecchio=super().get_nome()
        risultato=""
        for i in range(len(nome_vecchio)):
            if i % 2==0:
                risultato+=nome_vecchio[i].lower()
            else:
                risultato+=nome_vecchio[i].upper()

        return f"Mostro: {risultato}"



def pariUguali(a:list[int],b:list[int]):
    c:list=[]
    for i in range(len(a)):
        if a[i] % 2 == 0 and b[i] % 2 == 0:
            c.append(1)
        else:
            c.append(0)

    return c


def combattimento (a:Alieno, m:Mostro):
    vincitore=None
    if not isinstance (a,Alieno) or not isinstance(m,Mostro):
        print ("Battaglia non valida!")
        return vincitore
    else:
        c=pariUguali(a.get_munizioni(),m.get_assalto())
        counter=0
        for num in c:
            if num==1:
                counter+=1
        if counter>4:
            print (m.get_vittoria())
            print (m.get_vittoria())
            print (m.get_vittoria())
            vincitore=m
            return vincitore
        else:
            print (m.get_sconfitta())
            vincitore=a
            return vincitore


def proclama_vincitore(c:Creatura):

    if isinstance(c,Alieno):
        print ("hanno vinto gli alieni!")
        print (c)

    if isinstance(c,Mostro):
        print ("hanno vinto i mostri!")
        print (c)




a = Alieno("Robot")
m = Mostro("gorthor", "RAHH", "ugh...")

vincitore = combattimento(a, m)

if vincitore is not None:
    proclama_vincitore(vincitore)
