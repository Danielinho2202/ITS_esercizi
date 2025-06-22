class Frazione:
    def __init__(self,num:float,den:float):
        self.set_den(den)
        self.set_num(num)
    
    def set_num(self,num:float):
        try:
            num= float(num)
            if num.is_integer():
                self.num=num
            else:
                print ("non è un intero, quindi diventa 13")
                self.num=13
        except:
            print ("Numeratore non valido, impostato a 13")
            self.num=13
        
    def set_den(self,den:float):
        try:
            den= float(den)
            if den.is_integer() and den!=0:
                self.den=den
            else:
                print ("non è un intero, quindi diventa 5")
                self.den=5
        except:
            print ("Denominatore non valido, impostato a 5")
            self.den=5
        
    def get_num(self):
        return self.num
    
    def get_den(self):
        return self.den
    
    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def value(self):
        result= round(self.num/self.den,3)
        return result
    

    
def mcd(x:int,y:int):
    list_div_x=[]
    list_div_y=[]
    x=int(abs(x))
    y=int(abs(y))
    if x!=0:
        for i in range (1,x//2+1):
            if x%i==0:
                list_div_x.append(i)
        list_div_x.append(x)
    if y!=0:
        for i in range (1,y//2+1):
            if y%i==0:
                list_div_y.append(i)
        list_div_y.append(y)
    if not list_div_x and not list_div_y:
        raise TypeError("Non puoi dividere zero e zero")
    elif not list_div_x:
        max_div=y
        return max_div
    elif not list_div_y:
        max_div=x
        return max_div

    max_div=1
    for n in list_div_x:
        if n in list_div_y and n>max_div:
            max_div=n
    return max_div





def semplifica(l:list[Frazione]):
    new_list=[]
    for f in  l:
        if mcd(f.get_num(),f.get_den())!=1.0:
            m=mcd(f.get_num(),f.get_den())
            f.set_num(f.get_num()/m)
            f.set_den(f.get_den()/m)
        new_list.append(f)
    return new_list



def fractionCompare(l:list[Frazione],ris:list[Frazione]):
    for i in range (len(l)):
        print (f"originale: {l[i].value()}, semplificata: {ris[i].value()}")
    

l = [Frazione(2.5,0),Frazione(1,2),Frazione(2,4),Frazione(3,5),Frazione(6,9),Frazione(4,7),Frazione(24,36),Frazione(12,36),Frazione(40,60),Frazione(5,11),Frazione(10,45),Frazione(42,78),Frazione(9,15)]
l_s=semplifica(l)
fractionCompare (l,l_s)


#da fare privato