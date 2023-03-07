def color(s: str) -> str:
    value: int = len(s)
    return f"\033[38;2;{value};{value};{value}m{s}\033[0m"