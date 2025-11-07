from enum import Enum

from common.exceptions_custom.InvalidGenreException import InvalidGenreException


class Genre(Enum):
    ACTION = "Action"
    AVENTURE = "Aventure"
    COMEDIE = "Comedie" #on va tricher un peu pour l'instant
    CRIME = "Crime"
    DRAME = "Drame"

    @staticmethod
    def from_index(index: str) :
        try:
            index = int(index) #moche
            return [g.value for i, g in enumerate(Genre) if index - 1 == i][0] #moche mais drole
        except Exception:
            raise InvalidGenreException