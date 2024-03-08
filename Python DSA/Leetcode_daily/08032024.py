# 3005. Count Elements With Maximum Frequency

from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums) -> int:
        hm = Counter(nums)
        hm = dict(sorted(hm.items(), key=lambda item: item[1], reverse=True ))
        sum, oldVal = 0, -1
        for key, value in hm.items():
            if (oldVal == value) or oldVal == -1 :
                oldVal = value
                sum += value
            else:
                break
        return sum
    
sol = Solution().maxFrequencyElements([1,2,2])
print(sol)