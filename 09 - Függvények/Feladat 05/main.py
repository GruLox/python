from consoleIO import get_str
from helpers import count_matches

word1: str = None
word2: str = None
matchCount: int = None

word1 = get_str()
word2 = get_str()

matchCount = count_matches(word1, word2)

print(matchCount)








