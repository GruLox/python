from consoleIO import *
from convert import convert

temperature: float = get_temperature()
unit = get_unit()

convertedTemp = convert(unit, temperature)

print(f"{temperature} Celsius = {convertedTemp} {unit}")
