class Movie:
    """ This class represents movie data """

    next_id: int = 30

    def __init__(self, titre: str, annee_production: int, genre: str, age_limite: int, is_update: bool =False):
        
        self._titre = titre
        self._annee_production = annee_production
        self._genre = genre
        self._age_limite = age_limite
        if not is_update:
            Movie.next_id +=1
            self._id = Movie.next_id

    def __str__(self):
        return f"{self.id}. Titre : {self._titre}, annee_production : {self._annee_production}, genre : {self._genre}, age limite : {self._age_limite}"