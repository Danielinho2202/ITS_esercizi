class Movie:
    def __init__(self,movie_id:str,title:str,director:str,is_rented:bool=False):
        self.movie_id=movie_id
        self.title=title
        self.director=director
        self.is_rented=is_rented
    def rent(self) ->None:
        if self.is_rented == False:
            self.is_rented=True
        else:
            print ("Il film '{self.title}' è già noleggiato.")
    def return_movie(self):
        if self.is_rented == True:
            self.is_rented= False
        else:
            return "Il film '{self.title}' non è stato noleggiato."
        
class Customer:
    def __init__(self,customer_id,name:str):
        self.customer_id=customer_id
        self.name=name
        self.rented_movies:list[Movie]=[]

    def rent_movie(self,movie:Movie):
        if not movie.is_rented:
            movie.rent()
            self.rented_movies.append(movie)
        else:
            print("film affittato")

    def return_movie(self,movie:Movie):
        if movie in self.rented_movies:
            movie.return_movie()
            self.rented_movies.remove(movie)
        else:
            ("film non è stato affittato")

class VideoRentalStore:
    def __init__(self,customers:dict[str,Customer]={},movies: dict[str,Movie]={}):
        self.movies=movies
        self.customers=customers

    def add_movie(self,movie_id,title,director):

        if movie_id in self.movies:

            print ("Errore, è già nel catalogo")

        else:
            movie:Movie =Movie(movie_id,title,director)
            self.movies[movie_id] = movie

    def register_customer(self,customer_id:str,name:str):

        if customer_id in self.customers:
            print("jdhdjdj")
        else:
            customer:Customer =Customer(customer_id,name)
            self.customers[customer_id]=customer

    def rent_movie (self, customer_id,movie_id):
        if customer_id in self.customers and movie_id in self.movies:
            self.customers[customer_id].rent_movie(self.movies[movie_id])
        else:
            print("film non trovato")
    def rent_movie (self, customer_id,movie_id):
        if customer_id in self.customers and movie_id in self.movies:
            self.customers[customer_id].return_movie(self.movies[movie_id])
        else:
            print("film non trovato")
    #in più fatta in classe
    def get_rented_movies_store(self):
        lista:list=[]
        for cliente in self.customers.values():
            lista += cliente.rented_movies
            



        
    


