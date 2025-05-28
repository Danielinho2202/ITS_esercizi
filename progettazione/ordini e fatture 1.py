from typing import Any
import re
from datetime import date

class Indirizzo:
    def __init__(self,via,civico,cap):
        if via is None:
            raise ValueError(f"errore")
        if civico is None:
            raise ValueError
        if cap is None:
            raise ValueError
        self.via:str=via

        if not re.search("^[0-9]+[a-z]*$",civico):
            raise ValueError
        if not re.search("^\d[5]$",cap):
            raise ValueError
        self.civico=civico
        self.cap=cap

    def get_via(self):
        return self.via
    def get_civico(self):
        return self.civico
    def get_cap(self):
        return self.cap
    def __repr__(self):
        return f"Indirizzo (via={self.via}, civico={self.civico}), cap={self.cap}"

class Dipartimento:
    nomi_usati=set()
    def __init__(self,nome,indirizzo:Indirizzo):
        if not nome and nome in Dipartimento.nomi_usati:
            raise ValueError
        self.nome = nome
        self.indirizzo= indirizzo
        

        def __str__(self):
            return f"dipartimento {self.nome}, {self.indirizzo}"
        
class Direttore:
    codice_fiscale_usato=set()
    def __init__(self,nome,cognome,cf,data_nascita:date,anni_servizio:int):
        self.nome=nome
        self.cognome=cognome
        if cf in Direttore.codice_fiscale_usato:
            raise ValueError
        if not re.search("^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$", cf):
            raise ValueError
        self.cf=cf
        if data_nascita>date.today():
            raise ValueError
        self.data_nascita=data_nascita
        self.anni_servizio=anni_servizio

    def __str__(self):
        return f"Direttore {self.nome} {self.cognome}, CF: {self.cf}, nato il {self.data_nascita}, anni di servizio: {self.anni_servizio}"


