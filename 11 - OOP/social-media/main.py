from socialMediaPlatform import SocialMediaPlatform
from post import Post
from user import User

sanyi = User("Sanyi", "sanyi@gmail.com", "sanyi123")

reddit = SocialMediaPlatform("Reddit", sanyi)

post = Post("Hello", "Hello World", sanyi)

reddit.createPost(post)

print(reddit.name)



