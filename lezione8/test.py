from persona import Persona
from studente import Studente

p1: Persona = Persona("Daniele", "Gallo", 21)
print(p1)

st1: Studente = Studente("Cris", "Ronaldo", 38, "62863946")
print(st1)



'''if isinstance(st1, Studente):
    #true se fa parte, sennò false
    print ("st1 è istanza della classe Studente")

if isinstance(st1,Persona):
    #st1 è istanza anche di Persona
    print ("st1 è istanza di Persona")

if isinstance(p1,Persona):
    print ("p1 è istanza della classe Persona")

if isinstance(p1,Studente):
    print ("p1 è istanza della classe Studente")
else:
    print ("p1 non è istanza della classe Studente")

#studente è sottoclasse di persona?

if issubclass(Studente,Persona):
    print ("la classe Studente è sottoclasse della classe Persona")'''

#print (f"la media dello studente è {st1.get_media_esami[10,20,30]}")

st2:Studente = Studente(p1.get_name(), p1.get_lastname(), p1.get_age(), '5376339')
print(st2)

#confrontare se studente 1==p
print (st1==p1)

#confronto studente1 e studente2
print (st1==st2)

#verifichiamo se studente1 è uguale a se stesso
print (st1==st1)


#modificare nome, cognome età dello studente 2 per fargli avere gli stessi attributi)
st2.set_name(st1.get_name())
st2.set_lastname(st1.get_lastname())
st2.set_age(st1.get_age())
#confronto tra i 2 ora
print (st1==st2)
#forzo lo studente 2 ad avere la stessa media
st2.setMatricola(st1.getMatricola())
print (st1==st2)


