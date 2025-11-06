from exceptions_custom import InvalidTitleException, InvalidYearException,InvalidGenreException, InvalidAgeLimitException
from models.Movie import Movie
import csv

def show_movies_menu():
    rows = __read_rows()
    for row in rows:
        print(row)

def add_movie(titre, annee_production, genre, age_limite):
    movie = Movie(titre, annee_production, genre, age_limite)
    movie_file = open("write/data/movies.csv", "a")
    movie_file.write(__format_csv(movie))

def update_movie(id: int, titre, annee_production, genre, age_limite):
        rows = __read_rows()
        rows[id] = [id,titre,annee_production,genre,age_limite]
        __write_rows(rows)

def remove_movie(id: int):
    rows = __read_rows()
    rows.pop(id)
    __write_rows(rows)

def __read_rows():
    with open("write/data/movies.csv", "r", newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        return list(reader)
    
def __write_rows(rows: list):
    with open("write/data/movies.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def __format_csv(movie: Movie, id=None):
    return f"{id or movie._id},{movie._titre},{movie._annee_production},{movie._age_limite}\n"


def modify_movie_menu(id: int):
    title = is_valid(input_title)
    year = is_valid(input_production_year)
    genre = is_valid(input_production_genre)
    age_limite = is_valid(input_age)
    update_movie(id, title, year, genre, age_limite)


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

show_movies_menu()
