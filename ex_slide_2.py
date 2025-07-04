#docker exec -it its_postgresql psql -U postgres

def combinazione(testo:str):
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


def codifica(testo_originale,n):
        i=1
        if n==0:
            return testo_originale
        else:
            while i<=n:
                if i==1:
                    nuovo=combinazione(testo_originale)
                    i+=1
                else:
                    nuovo=combinazione(nuovo)
                    i+=1
        return nuovo

s="abcde"
print (codifica(s,1))