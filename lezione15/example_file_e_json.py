#PATH: str = "lezione15/example.txt"

#file= open(PATH, "r", encoding="utf-8")
#output= file.read()
#print (output)
#file.close()

#file = open("lezione15/example.txt", "a")
#try:
#    pass
#except:
#    pass
#finally:
#    file.close()

#with open("lezione15/example.txt", "r") as file:
#    print(file.read())
import json

file =open("lezione15/config.json","w")

db: dict ={"DNISNCSN": {"Name":"CMOSC","Surname":"KWNWNSNNW"},
          "NSCNNNNDJ":{"Name":"NCIWNI","Surname":"DMDDKDK"}}

json.dump(db, file)

file.close()