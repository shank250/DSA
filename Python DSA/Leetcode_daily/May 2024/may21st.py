class Solution:
    ans = set()
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        def backTrack(self, nums, depth):
            if depth == 1: return
            self.ans.add(str(nums))
            for i in range(len(self.ans)):
                print(nums)
                tmp = nums.copy()
                backTrack(self, nums.pop(i), depth - 1)
        backTrack(self, nums=nums, depth=len(nums))
        print(ans)
        return list(self.ans)
obj = Solution().subsets([1,2,3])


            