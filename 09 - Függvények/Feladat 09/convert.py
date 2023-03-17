EUR: float = 400
JPY: float = 0.75 * EUR
USD: float = 0.8 * EUR
CHF: float = 0.55 * EUR

def convert(currency: str, amount: float) -> float:
    if (currency not in ["EUR", "JPY", "USD", "CHF"]):
        print("Invalid currency")
        return None
    else:
        match currency:
            case "EUR":
                return round(amount / EUR, 2)
            case "JPY":
                return round(amount / JPY, 2)
            case "USD":
                return round(amount / USD, 2)
            case "CHF":
                return round(amount / CHF, 2)

    
