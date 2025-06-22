def check_dna(s1:str,s2:str):
    s2_r=""
    s2_r+= s2 [::-1]
    return s2_r

def equal_dna(s1,s2):
    x=s1[-6:-1]
    x+=s1[-1]
    y=s2[0:6]
    counter=0
    max_s=0
    for i in range (0,len(x),-1):
        if x[i]==y[i]:
            counter+=1
            if counter>max_s:
                max_s=counter
        else:
            counter=0
    return max_s




s1= "GGTACCGTGA"
s2= "CGTGAACCTT"

print (equal_dna(s1,s2))






