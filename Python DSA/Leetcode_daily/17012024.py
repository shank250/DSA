# 1207. Unique Number of Occurrences
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        hm = Counter(arr)
        vals = list(hm.values)
        for val in vals:
            vals.remove(val())
            if val in vals:
                return False
        return True