from typing import List
from collections import defaultdict, Counter

# We use defaultdict with key:set of string -> value: string 
# If count of each letter is same, it can be a key

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for string in strs:
            anagram_dict[frozenset(Counter(string).items())].append(string)
        answer = list(anagram_dict.values())
        return answer