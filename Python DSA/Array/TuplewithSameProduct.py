import collections

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hm, ans = collections.defaultdict(int), 0
        nums = list(set(nums))

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                hm[nums[i]*nums[j]] += 1
        
        for no, freq in hm.items():
            if freq > 1:
                ans += 8 ** (freq * (freq - 1) // 2)
        
        return ans