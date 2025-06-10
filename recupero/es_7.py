class ContactManager:
    def __init__(self,contacts:dict[str,list[str]]):
        self.contacts=contacts

    def  create_contact(self,name:str,phone_numbers:list[str]):
        if name not in self.contacts:
            self.contacts[name] = phone_numbers
            return {name:self.contacts[name]}
        else:
            return "Errore: contatto già esiste"
        
    def add_phone_number(self,contact_name:str , phone_number:str):
        if contact_name not in self.contacts:
            return "Errore: Contatto non esiste"
        elif phone_number in self.contacts[contact_name]:
            return "Errore: Numero già esistente"
        else:
            self.contacts[contact_name].append(phone_number)
            return {contact_name:self.contacts[contact_name]}

    def remove_phone_number(self,contact_name:str,phone_number:str):
        if contact_name not in self.contacts:
            return "Errore: Contatto non esiste"
        elif phone_number not in self.contacts[contact_name]:
            return "Errore: Numero non esistente per questo contatto"
        else:
            self.contacts[contact_name].remove(phone_number)
            return {contact_name:self.contacts[contact_name]}

    def update_phone_number(self,contact_name : str, old_phone_number:str,new_phone_number):
        if contact_name not in self.contacts:
            return "Errore: Contatto non esiste"
        elif old_phone_number not in self.contacts[contact_name]:
            return "Errore: Numero non esistente per questo contatto"
        elif new_phone_number in self.contacts[contact_name]:
            return "Errore: Numero già esistente"
        else:
            self.contacts[contact_name].remove(old_phone_number)
            self.contacts[contact_name].append(new_phone_number)
            return {contact_name:self.contacts[contact_name]}
    def list_contacts(self) ->list:
        lista_contatti:list=[]
        for key in self.contacts.keys():
            lista_contatti.append(key)
        return lista_contatti
    def list_phone_number(self,contact_name):
        if contact_name not in self.contacts:
            return "Errore: Contatto non esiste"
        else:
            return self.contacts[contact_name]
    def search_contact_by_phone_number(self,phone_number:str):
        lista_contatti:list=[]
        for keys in self.contacts.keys():
            if phone_number in self.contacts[keys] :
                lista_contatti.append(keys)

        if lista_contatti:
            return lista_contatti
        else:
            return "Errore, nessun numero corrispondente"






# Creazione dell'oggetto ContactManager con dizionario vuoto
manager = ContactManager({})

print(manager.create_contact("Mario Rossi", ["1234567890"]))
# Output: {"Mario Rossi": ["1234567890"]}

print(manager.add_phone_number("Mario Rossi", "0987654321"))
# Output: {"Mario Rossi": ["1234567890", "0987654321"]}

print(manager.remove_phone_number("Mario Rossi", "1234567890"))
# Output: {"Mario Rossi": ["0987654321"]}

print(manager.update_phone_number("Mario Rossi", "0987654321", "1112223333"))
# Output: {"Mario Rossi": ["1112223333"]}

print(manager.list_contacts())
# Output: ["Mario Rossi"]

print(manager.list_phone_number("Mario Rossi"))
# Output: ["1112223333"]

print(manager.search_contact_by_phone_number("1112223333"))
# Output: ["Mario Rossi"]


    

        
