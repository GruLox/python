from consoleIO import getAmount, getCurrency
from convert import convert

EUR: float = 400
JPY: float = 0.75 * EUR
USD: float = 0.8 * EUR
CHF: float = 0.55 * EUR

amount: float = getAmount()
currency: str = getCurrency()

convertedAmount: float = convert(currency, amount)

print(convertedAmount, currency)

