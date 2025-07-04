from abc import ABC,abstractmethod
from string import ascii_lowercase

class CodificatoreMessaggio(ABC):
    @abstractmethod
    def codifica(testo_originale:str):
        pass

class DecodificatoreMessaggio(ABC):
    @abstractmethod
    def decodifica(testo_codificato):
        pass

class CifratoreAScorrimento(CodificatoreMessaggio,DecodificatoreMessaggio):
    def __init__(self,key):
        self.key=key

    def codifica(self,testo_originale):
        alpha=list(ascii_lowercase)
        alpha_m=list(ascii_lowercase.upper())

        s_result:str=""

        for let in testo_originale:
            if let in alpha:
                new_let=alpha[(alpha.index(let)+self.key)%26]
                s_result+=new_let
            elif let in alpha_m:
                new_let=alpha_m[(alpha_m.index(let)+self.key)%26]
                s_result+=new_let
            else:
                s_result+=let
        return s_result
    
    def decodifica(self,testo_codificato):
        alpha=list(ascii_lowercase)
        alpha_m=list(ascii_lowercase.upper())

        s_result:str=""

        for let in testo_codificato:
            if let in alpha:
                new_let=alpha[(alpha.index(let)-self.key)%26]
                s_result+=new_let
            elif let in alpha_m:
                new_let=alpha_m[(alpha_m.index(let)-self.key)%26]
                s_result+=new_let
            else:
                s_result+=let
        return s_result
    

class CifratoreACombinazione(CodificatoreMessaggio,DecodificatoreMessaggio):
    
    def __init__(self,n):
        self.n=n


    def _combinazione(self,testo:str):
        meta=""
        s_meta=""
        if len(testo)%2==0:
            for i in range (len(testo)):
                if i<len(testo)//2:
                    meta+=testo[i]
                if i>=len(testo)//2:
                    s_meta+=testo[i]
        if len(testo)%2!=0:
            for i in range (len(testo)):
                if i<(len(testo)+1)//2:
                    meta+=testo[i]
                if i>=(len(testo)+1)//2:
                    s_meta+=testo[i]
        risultato=""
        for i in range (len(meta)):
            try: 
                if s_meta[i]:
                    risultato+=meta[i]
                    risultato+=s_meta[i]
            except IndexError:
                risultato+=meta[i]
        return risultato
    
    def codifica(self, testo_originale):
        if self.n == 0:
            return testo_originale

        nuovo = testo_originale
        i = 0
        while i < self.n:
            nuovo = self._combinazione(nuovo)
            i += 1
        return nuovo

    def decodifica(self,testo_codificato):
        if self.n==0:
            return testo_codificato
        m=0
        while m<self.n:
            meta=""
            s_meta=""
            for i in range (len(testo_codificato)):
                if i%2==0:
                    meta+=testo_codificato[i]
                else:
                    s_meta+=testo_codificato[i]
            testo_codificato= meta+s_meta
            m+=1
        return testo_codificato
            
            


