#es.2-3
(name) = str(input("inserisci il tuo nome"))
print (f"Hey {name} , where are you from?")
#2-4
print(name.lower())  
print(name.upper()) 
print(name.title()) 
#2-6
quote:str = ("i like computers!")
famous_person = ("Daniele")
print(f"{famous_person} disse: {quote}" )

#lower o upper si usa per cercare di comparare le stringhe
#per visualizzare le virgolette: 
# 2 modi: (f"{famous_person} disse: \"{quote}\"" )
#(f"{famous_person} disse: {quote}" )
