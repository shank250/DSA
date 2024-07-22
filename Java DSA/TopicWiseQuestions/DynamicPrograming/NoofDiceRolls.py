class Solution:
    def __init__(self) -> None:
        self.val = 0
    # val = 0
    def find(self, n, k, target, dp, newN, newK):
        if newN < 0: return 0
        if newK < 0: return 0
        if newK == 0 and newN == 0: return 1 # and newN == 0
        print(newN, newK)
        if dp[newN][newK] != -1: 
            return dp[newN][newK] #if revisited

        start = min(target, k)

        for i in range(start, 0, -1):
            val += self.find(self, n, k, target, dp, newN - 1, newK - i)

        dp[newN][newK] = val
        return val

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[-1]*(max(target, k) + 1) for _ in range(n + 1)]
        print(dp[1][6])
        print(self.find(self, n, k, target, n, k))
        return 0

sol = Solution()
sol.numRollsToTarget(1, 6, 3)