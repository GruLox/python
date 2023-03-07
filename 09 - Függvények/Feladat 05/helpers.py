def count_matches(s1: str, s2: str) -> int:
    counter: int = 0
    matches: str = ""
    for i in s1:
        for j in s2:
            if (i == j and  j not in matches):
                counter += 1
                matches += j
    
    return counter