from consoleIO import *
from helpers import calculateAge

name: str = None
birthyear: int = None

name = getName()
birthyear = getBirthYear()
age = calculateAge(birthyear)
print(f"{name} ön az idén {age} éves")







