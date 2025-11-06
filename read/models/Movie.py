class Movie:
    """ This class represents movie data """

    id: int = 30

    def __init__(self, titre: str, annee_production: int, genre: str, age_limite: int):
        self._titre = titre
        self._annee_production = annee_production
        self._genre = genre
        self._age_limite = age_limite
        Movie.id += 1

    def __str__(self):
        return f"Titre : {self._titre}, annee_production : {self._annee_production}, genre : {self._genre}, age limite : {self._age_limite}"
