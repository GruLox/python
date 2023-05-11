from user import User


class Post:
    def __init__(self, title: str, content: str, author: User):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"{self.title}, {self.author.name}"