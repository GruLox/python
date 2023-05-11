class User:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, newPassword: str):
        self.password = newPassword

    def __str__(self):
        return f"név={self.name}, email={self.email}, jelszó={self.password}"