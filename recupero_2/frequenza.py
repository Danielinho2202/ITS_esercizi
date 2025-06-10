
def freq(s:str) ->dict:
    conteggio:dict={}
    lista_token=[]
    token=""
    for char in s:
        if char != ' ':
            token+=char
        else:
            token_pulito=token.strip(".?,!;: ")
            lista_token.append(token_pulito)
            token=""

    for token in lista_token:
        if token:
            if token not in conteggio:
                conteggio[token]=1
            else:
                conteggio[token]+=1
    return conteggio

print (freq("Hello, world! Hello... PYTHON? world."))


