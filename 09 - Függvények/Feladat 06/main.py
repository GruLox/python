from consoleIO import *
from convert import convert

temperature: float = getTemperature()
unit = getUnit()

convertedTemp = convert(unit, temperature)

print(f"{temperature} Celsius = {convertedTemp} {unit}")
