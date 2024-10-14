# 1657. Determine if Two Strings Are Close

from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        hm1 = Counter(word1)
        hm2 = Counter(word2)

        if set(hm1.keys())==set(hm2.keys()) and sorted(hm1.values())==sorted(hm2.values()):
            return True
        return False