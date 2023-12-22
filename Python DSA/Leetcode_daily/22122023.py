# 1422. Maximum Score After Splitting a String
# Easy
# Topics
# Companies
# Hint

# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

class Solution:
    def maxScore(self, s: str) -> int:
        nums = [x for x in s]
        rtnMax = 0
        for i in range(1, len(nums)):
            zeroCnt = 0
            oneCnt = 0
            for k in range(i):
                if nums[k] == "0":
                    zeroCnt += 1
            for j in range(i, len(nums)):
                if nums[j] == "1":
                    oneCnt += 1
            
            if (zeroCnt + oneCnt) > rtnMax:
                rtnMax = (zeroCnt + oneCnt)
        return rtnMax
            