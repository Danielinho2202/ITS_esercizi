'''Start with your program from Exercise 8-7. Write a while loop that allows users 
to enter an album’s artist and title. Once you have that information, 
call make_album() with the user’s input and print the dictionary that’s created.
 Be sure to include a quit value in the while loop.'''

def make_album(name:str, title:str, numero_canzoni=None):
    album:dict={"nome":name,"titolo":title,"numero canzoni":numero_canzoni}
    return (album)

risposta=str(input("vuoi inserire un'album? "))
while risposta=="si":
    name=str(input("inserisci nome artista: "))
    title=str(input("inserisci nome album: "))
    numero_canzoni=int(input("inserisci numero canzoni "))
    print (make_album(name,title,numero_canzoni))
    risposta=str(input("vuoi inserire un'album? "))



