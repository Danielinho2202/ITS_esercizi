'''Scrivere un programma in Python che memorizzi il nome, il ruolo e l'età di un utente 
in un dizionario. Il nome, il ruolo e l'età devono essere inseriti in input dall'utente 
stesso. Il programma deve determinare il livello di accesso ai servizi in base al ruolo 
e all'età dell'utente secondo questo schema:

- Admin → "Accesso completo a tutte le funzionalità."
- Moderatore → "Può gestire i contenuti ma non modificare le impostazioni."
- Utente adulto (età ≥ 18) → "Accesso standard a tutti i servizi."
- Utente minorenne (età < 18) → "Accesso limitato! Alcune funzionalità sono bloccate."
- Ospite → "Accesso ristretto! Solo visualizzazione dei contenuti."
- Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! Accesso Negato!'''

info={}
nome_utente=str(input("Digita nome utente: ")).title()
ruolo=str(input("Digitare ruolo dell'utente: ")).lower()
age=int(input("Digitare età dell'utente: "))

info["ruolo"]= ruolo
info["età"]= age

match info:
    case info if info["ruolo"]== "admin":
        print (f"ciao {nome_utente}, hai accesso a tutte le funzionalità!")
    case info if info["ruolo"]== "moderatore":
        print (f"Ciao {nome_utente},puoi gestire i contenuti ma non puoi modificare le impostazioni")
    case info if info["ruolo"]== "utente":
        if info["età"]>=18:
            print (f"Ciao {nome_utente}, accesso standard a tutti i servizi!")
        else:
            print (f"Ciao {nome_utente} alcune funzionalità sono bloccate!")
    case info if info["ruolo"]== "ospite":
        print (f"Ciao {nome_utente}, accesso ristretto!")
    case _:
        print ("Attenzione! Ruolo non riconosciuto!")
        




