from user import User
from post import Post

class SocialMediaPlatform:
    def __init__(self, name: str, users=None) -> None:
        self.name = name
        self.users: list[User] = users if users else []
        self.posts:  list[Post] = []

    def addUser(self, user: User) -> None:
        self.users.append(user)

    def createPost(self, post: Post) -> None:
        self.posts.append(post)