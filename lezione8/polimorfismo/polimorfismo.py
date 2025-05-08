from persona import Persona
from alieno import Alieno

#creiamo oggetto p (persona)
p:Persona = Persona("Daniele","Gallo",21)

#vediamo info persona
print (p)

#creare oggetto et della classe alieno
et:Alieno=Alieno("Andromeda")
print(et)

#oggetto p invoca speak
p.speak()
#oggetto et invoca speak
et.speak()
#ricorda polimorfismo, è questo
#c'è anche l'Overriding , è lo stesso concetto,
#ma con la differenza 