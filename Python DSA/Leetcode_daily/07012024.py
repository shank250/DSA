nums = [2,4,6,8,10]

n = len(nums)
counter = 0
for i in range(n):
    for j in range(n):
        if i == j:
            pass
        else:
            a = nums[i]
            b = nums[j]
            c = nums[j] - (nums[i] - nums[j])
            if c in nums:
                print(a, b, c)
                counter += 1
print(counter)

class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        total, n = 0, len(nums)
        dp = [{} for _ in nums]
        for i in range(1, n):
            for j in range(i):
                diff = nums[j] - nums[i]
                dp[i][diff] += dp[j][diff] + 1
                total += dp[j][diff]
        return total
    