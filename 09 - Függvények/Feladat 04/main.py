from consoleIO import getName
from helpers import color

name: str = None

name = getName()
name = color(name)
print(f"Üdvözlöm, {name}")

