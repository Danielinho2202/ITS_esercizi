#4-10
'''lista= list(range(3,31,3))
print (f"the first three itemsin the lista are: {lista[:3]}")
print (f"the 3 terms in the middle are: {lista[3:6]}")
print (f"the last 3 number are: {lista[-3:]}")'''

#4-11
pizze:list= ["margherita","boscaiola","diavola"]
friend_pizzas= ["margherita","boscaiola","diavola"]

pizze.append("marinara")
friend_pizzas.append("wurstel e patate")

result= ", ".join(pizze)
print (f"my favourite pizzas are: {result}")

print (f"my friend's favourite pizza are: ")
for pizza in friend_pizzas:
    print (pizza)
