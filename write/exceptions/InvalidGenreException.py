class InvalidGenreLimitException(Exception):

    def __init__(self, message=None):
        self.message = message or f"Genre invalide"
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"