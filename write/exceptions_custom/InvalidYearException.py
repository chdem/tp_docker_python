class InvalidYearException(Exception):

    def __init__(self, message=None):
        self.message = message or f"Année de production invalide"
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"