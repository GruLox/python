from consoleIO import getStr
from helpers import countMatches


word1: str = getStr()
word2: str = getStr()

matchCount: int = countMatches(word1, word2)

print(matchCount)








