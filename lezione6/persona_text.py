'''from persona import Persona
#abbiamo importato la persona dell'altra cartella

dg:Persona= Persona("Daniele", "Gallo", 21)
print(dg)
print(dg.name,dg.lastname,dg.age)
#richiamare la funzione displaydata dalla calsse persona per mostrare in output i dati
dg.displayData()'''


from persona2 import Persona

dg:Persona = Persona()

#richiamo la funzione display data per mostare le informazioni di fm
#dg.displayData()
#print("-----------------")
dg.setname("Daniele")
dg.setlastname("Gallo")
dg.setage(1)

dg.displayData()

print("-----------------")

print(dg.getname(),dg.getlastname(),dg.getage())



