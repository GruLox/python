from consoleIO import get_name
from helpers import *

name: str = None
birthyear: int = None

name = get_name()
birthyear = get_birth_year()
age = calculate_age(birthyear)
print(f"{name} ön az idén {age} éves")







