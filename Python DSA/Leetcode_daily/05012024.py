# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
        # max_ss = 0
        # counter = 0
        # for i in nums:
        #     if i == nums[0]:
        #         prev = i
        #     else:
        #         if prev < i:
        #             counter += 1
        #             if counter > max_ss:
        #                 max_ss = counter
        #         else:
        #             counter = 0
        # return max_ss
        # def lengthOfLIS(nums):
nums = [3,4,5,2]
if not nums:
    # return 0
    print(0)
n = len(nums)
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# return max(dp)
print(max(dp))