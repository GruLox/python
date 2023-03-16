from consoleIO import getStr
from helpers import countMatches

word1: str = None
word2: str = None
matchCount: int = None

word1 = getStr()
word2 = getStr()

matchCount = countMatches(word1, word2)

print(matchCount)








