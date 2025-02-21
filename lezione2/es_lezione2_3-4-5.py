#3.4
name:list= ["daniele", "pietro", "giorgia"]
print (f"Hey {name[0]}, vuoi venire alla cena?" )
print (f"Hey {name[1]}, vuoi venire alla cena?" )
print (f"Hey {name[2]}, vuoi venire alla cena?" )
#3.5
print (f"{name[2]} non può venire a cena")
name.pop(2)
name.insert(2,"lavinia")
print (f"{name[0]}, vuoi venire alla cena?" )
print (f"{name[1]}, vuoi venire alla cena?" )
print (f"{name[2]}, vuoi venire alla cena?" )
#3.6
print (f"{name[0]}, ho trovato un tavolo più grande, invito altre persone" )
print (f"{name[1]}, ho trovato un tavolo più grande, invito altre persone" )
print (f"{name[2]}, ho trovato un tavolo più grande, invito altre persone" )
name.insert(0,"beatrice")
meta=len(name)//2
name.insert(meta,"lorenzo")# variabile meta per metterlo al centro
name.append("stefano")
print (f"Hey {name[0]}, vuoi venire alla cena?" )
print (f"Hey {name[1]}, vuoi venire alla cena?" )
print (f"Hey {name[2]}, vuoi venire alla cena?" )
print (f"Hey {name[3]}, vuoi venire alla cena?" )
print (f"Hey {name[4]}, vuoi venire alla cena?" )