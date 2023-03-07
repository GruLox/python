from consoleIO import get_name
from helpers import color

name: str = None

name = get_name()
name = color(name)
print(f"Üdvözlöm, {name}")    

