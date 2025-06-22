
def check_integer(n:float):
    while not n.is_integer() or n<0:
        print ("numero deve essere intero e positivo")
        n=float(input("riprova: "))
    return n

x=float(input("x= "))
x=check_integer(x)


l=[]
l_s=float(input("inserisci un numero per fare una sequenza, 0 per terminare: "))
l_s=check_integer(l_s)
while l_s!=0:
    l.append(int(l_s))
    l_s=float(input("unaltro numero, 0 per terminare: "))
    l_s=check_integer(l_s)


def seq(x,l:list[int]):
    print (l)
    counter=0
    somma=0
    for i in range (len(l)):
        if l[i] == x:
            if counter == 0:
                pos=i
            counter +=1
        else:
            somma+=l[i]
    print (f"{x} compare {counter} volte nella sequenza")
    print (f"il primo valore uguale a x sta in posizione {pos}")
    print (somma)

            
            
print (seq(x,l))