def count_matches(s1: str, s2: str) -> int:
    matches: str = ""
    for i in s1:
        for j in s2:
            if (i == j and j not in matches):
                matches += j
    
    return len(matches)