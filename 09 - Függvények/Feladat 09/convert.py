EUR: float = 400
JPY: float = 0.75 * EUR
USD: float = 0.8 * EUR
CHF: float = 0.55 * EUR

def convert(ticker: str, amount: float):
    if (ticker not in ["EUR", "JPY", "USD", "CHF"]):
        print("Invalid ticker")
        return None
    else:
        match ticker:
            case "EUR":
                return amount / EUR
            case "JPY":
                return amount / JPY
            case "USD":
                return amount / USD
            case "CHF":
                return amount / CHF

    
