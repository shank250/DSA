# # // 1155. Number of Dice Rolls With Target Sum
# // Solved
# // Medium
# // Topics
# // Companies
# // Hint

# // You have n dice, and each die has k faces numbered from 1 to k.

# // Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # def numRollsToTarget(n, k, target):
        MOD = 10**9 + 7
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                for p in range(1, k + 1):
                    if j - p >= 0:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - p]) % MOD

        return dp[n][target]