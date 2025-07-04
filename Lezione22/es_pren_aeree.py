from abc import ABC, abstractmethod
from __future__ import annotations

class Volo(ABC):
    _codice_volo:str
    _max_cap:int
    _prenotazioni:int #0
    def __init__(self,_codice_volo, _max_cap):
        self._codice_volo=_codice_volo
        self._max_cap=_max_cap
        self._prenotazioni=0

    @abstractmethod
    def prenota_posto(self,posti):
        pass
        
    @abstractmethod
    def posti_disponibili(self):
        pass
        

class VoloCommerciale(Volo):
    def __init__(self, _codice_volo, _max_cap):
        super().__init__(_codice_volo, _max_cap)
        self.posti_economy=int(_max_cap*0.70)
        self.posti_business=int(_max_cap*0.20)
        self.posti_prima=int(_max_cap*0.10)
        self.pren_economy=0
        self.pren_business=0
        self.pren_prima=0


    def posti_disponibili(self):
        tot_disp = self._max_cap - self._prenotazioni
        econ_disp = self.posti_economy - self.pren_economy
        bus_disp = self.posti_business - self.pren_business
        pri_disp = self.posti_prima - self.pren_prima
        
        ris:dict={"posti diponibili" : tot_disp, "posti economy":econ_disp, 
                  "posti business":bus_disp, "posti prima classe": pri_disp}
        
        return ris
    

    def prenota_posto(self, posti:int, classe_servizio:str):
        if posti <= 0:
            print ("prenota almeno un posto")
            return
        
        
        if self.posti_disponibili()["posti disponibili"]<posti:
            print ("Il volo è al completo!")
            return

        match classe_servizio:
            case "economica":
                if self.posti_disponibili()["posti economy"]<posti:
                    print ("non ci sono posti in economy!")
                    return
                self.pren_economy+=posti

            case "business":
                if self.posti_disponibili()["posti business"]<posti:
                    print ("non ci sono posti in business!")
                    return
                self.pren_business+=posti

            case "prima":
                if self.posti_disponibili()["posti prima classe"]<posti:
                    print ("non ci sono posti in prima!")
                    return
                self.pren_prima+=posti
            case _:
                print (f"Non esiste una categoria {classe_servizio}")
                return


class VoloCharter(Volo):

    def __init__(self, _codice_volo, _max_cap, costo_volo:float):
        super().__init__(_codice_volo, _max_cap)
        self.costo_volo=costo_volo

    def prenota_posto(self):
        if self._prenotazioni==0:
            self._prenotazioni= self._max_cap
            print (f"Il volo {self._codice_volo} è stato prenotato, con prezzo di {self.costo_volo*self._max_cap}")
        else:
            print ("Volo già prenotato")

    def posti_disponibili(self):
        if self._prenotazioni==0:
            return self._max_cap
        else:
            return 0
        
class CompagniaAerea:
    
    def __init__(self, nome, prezzo:float,):
        self.nome=nome
        self.prezzo=prezzo
        self.flotta:list=[]


    def aggiungi_volo(self,volo_commerciale:VoloCommerciale):
        if volo_commerciale not in self.flotta:
            self.flotta.append(volo_commerciale)
        else:
            print ("Aereo già nella flotta")
    
    def rimuovi_volo(self,volo_commerciale:VoloCommerciale):
        if volo_commerciale in self.flotta:
            self.flotta.remove(volo_commerciale)
        else:
            print ("Aereo non è nella flotta")

    def mostra_flotta(self):
        return self.flotta
    
    def guadagno(self):
        prezzo_standard = self.prezzo
        prezzo_business = self.prezzo * 2
        prezzo_prima = self.prezzo * 3
        totale = 0.0

        for volo in self.flotta:
            totale_standard = prezzo_standard * volo.pren_economy
            totale_business = prezzo_business * volo.pren_business
            totale_prima = prezzo_prima * volo.pren_prima
        
            totale += totale_standard + totale_business + totale_prima

        return round(totale, 2)


    