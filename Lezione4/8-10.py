'''Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints 
each text message and moves each message to a new list called sent_messages as it’s printed.
 After calling the function, print both of your lists to make sure the messages were moved correctly.'''


messaggi=["ciao","tutto bene?","wow!","acciderbolina!"]

def show_messages(messaggi):
    for messaggio in messaggi:
        print (messaggio)


def send_messages():
    messaggi_ricevuti:list=[]
    for messaggio in messaggi:
        print (messaggio)
        messaggi_ricevuti.append(messaggio)
    print (messaggi_ricevuti)
    print (messaggi)

send_messages()



