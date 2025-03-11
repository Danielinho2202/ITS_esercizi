'''Start with your work from Exercise 8-10. Call the function send_messages() 
with a copy of the list of messages. After calling the function,
 print both of your lists to show that the original list has retained its messages.'''

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
