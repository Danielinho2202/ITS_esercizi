from film import Film

class Noleggio:
    

    def __init__(self,film_list:list[Film]):

        self.film_list=film_list
        self.rented_film:dict[int,list[int]]={}


    def is_avaible(self,film:Film):
        for film_l in self.film_list:
            if film_l.isequal(film) == True:
                print ("Film disponibile!")
                return True
        print ("Film non disponibile.")
        return False
        
    def rentAMovie(self,film,clientId):
        if self.is_avaible(film) == False:
            return
        
        self.film_list.remove(film)

        if clientId not in self.rented_film:
            self.rented_film[clientId] = [film]
            print ("Titolo noleggiato!")
        else:
            self.rented_film[clientId] = film.append(film)
            print ("Titolo noleggiato!")

    def giveBack(self,film,clientId,days):
        if clientId not in self.rented_film:
            print ("Non c'è il cliente che hai scritto")
            return
        if film in self.rented_film[clientId]:
            self.rented_film[clientId].remove(film)
            self.film_list.append(film)
            print (f"Film restistuito a {clientId} con penale = {film.calcolaPenaleRitardo(days)} ") 
            return
        else:
            print ("Film non trovato.")

     