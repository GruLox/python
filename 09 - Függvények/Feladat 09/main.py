from consoleIO import getAmount, getCurrency
from convert import convert


amount: float = getAmount()
currency: str = getCurrency()

convertedAmount: float = convert(currency, amount)

print(convertedAmount, currency)

