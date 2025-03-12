'''Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints 
each text message and moves each message to a new list called sent_messages as it’s printed.
 After calling the function, print both of your lists to make sure the messages were moved correctly.'''

def show_messages(*messaggi:list):
    for messaggio in messaggi:
        print (messaggio)

#show_messages ("ciao","tutto bene?","wow!","acciderbolina!")


def send_messages(*messaggi:list):
    messages=(list(messaggi))
    messaggi_ricevuti:list=[]
    while len(messages)>0:
        
        print (messages[0])
        
        messaggi_ricevuti.append(messages[0])
        messages.pop(0)

    print (messaggi_ricevuti)
    print (messages)

send_messages("ciao","tutto bene?","wow!","acciderbolina!")



