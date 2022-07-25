import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub("[^a-zA-Z0-9]",' ',paragraph)
        #Ignore except alphanumeric letter
        words = [word.lower() for word in paragraph.split()]
        
        #In case counter does not preserver order
        freq_counter = sorted(list(Counter(words).items()) , key = lambda x: -x[1])
        for word, count in freq_counter:
            if word not in banned:
                return word