from string import ascii_lowercase

def caesar_cypher_encrypt(s:str,key:int):
    alpha=list(ascii_lowercase)
    alpha_m=list(ascii_lowercase.upper())

    s_result:str=""

    for let in s:
        if let in alpha:
            new_let=alpha[(alpha.index(let)+key)%26]
            s_result+=new_let
        elif let in alpha_m:
            new_let=alpha_m[(alpha_m.index(let)+key)%26]
            s_result+=new_let
        else:
            s_result+=let
    return s_result

s="abcdefghijklmnopqrstuvwxyz"
print(caesar_cypher_encrypt(s,25))

def caesar_cypher_decrypt(s:str,key:int):
    alpha=list(ascii_lowercase)
    alpha_m=list(ascii_lowercase.upper())

    s_result:str=""

    for let in s:
        if let in alpha:
            new_let=alpha[(alpha.index(let)-key)%26]
            s_result+=new_let
        elif let in alpha_m:
            new_let=alpha_m[(alpha_m.index(let)-key)%26]
            s_result+=new_let
        else:
            s_result+=let
    return s_result
            
s="zabcdefghijklmnopqrstuvwxy"
print(caesar_cypher_decrypt(s,25))
