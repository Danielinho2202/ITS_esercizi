def aumento(diz:dict[str:float]) ->dict:
    new_dic={}
    for key,value in diz.items():
        if value<50:
            value+= (value*10)/100
            new_dic[key] = round(value,2)
    return new_dic

diz:dict={"a":46.836489,"b":10,"c":56}
print (aumento(diz))


