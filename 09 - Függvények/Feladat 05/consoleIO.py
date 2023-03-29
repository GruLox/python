def get_str() -> str:
    s: str = None
    while (s == None or len(s) < 2):
            print(f"Kérem adjon meg egy szót: ", end="")
            s = input()
    
    return s
