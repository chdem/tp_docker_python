from exceptions_custom import InvalidTitleException, InvalidYearException,InvalidGenreException, InvalidAgeLimitException
from models.Movie import Movie


def add_movie(titre, annee_production, genre, age_limite):
    movie = Movie(titre, annee_production, genre, age_limite)
    movie_file = open("write/data/movies.csv", "a")
    movie_file.write(__format_csv(movie))


def __format_csv(movie: Movie):
    return f"{movie._id},{movie._titre},{movie._annee_production},{movie._age_limite}\n"


def add_movie_menu():
    title = is_valid(input_title)
    year = is_valid(input_production_year)
    genre = is_valid(input_production_genre)
    age_limite = is_valid(input_age)

    add_movie(title, year, genre, age_limite)

def is_valid(function):
    while True:
        try:
            return function()  
        except (InvalidTitleException.InvalidTitleException,
                InvalidYearException.InvalidYearException, 
                InvalidGenreException.InvalidGenreException, 
                InvalidAgeLimitException.InvalidAgeLimitException) as e:
            print(e)
        except Exception:
            print("Erreur lamentable, le programme s'arrête")
            exit()

def input_title():
    title = input("Entrez un titre de film : ")
    if title.strip() == "":
        raise InvalidTitleException.InvalidTitleException()
    return title

def input_production_year():
    prod_year = int(input("Entrez l'année de sortie : "))
    if not (1800 < prod_year <= 2025) :
        raise InvalidYearException.InvalidYearException()
    return prod_year
        
def input_production_genre():
    genre = input("Entrez le genre : ")
    if genre.strip() == "":
        raise InvalidGenreException.InvalidGenreException()
    return genre

def input_age():
    age = int(input("Entrez l'age minimum : "))
    if not (0 < age <= 18):
        raise InvalidAgeLimitException.InvalidAgeLimitException()
    return age


add_movie_menu()
