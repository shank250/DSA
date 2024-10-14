# 678. Valid Parenthesis String

s = "(*))"

class Solution:
    def checkValidString(self, s: str) -> bool:
        low, high = 0, 0
        for ch in s:
            if ch == "(":
                low, high = low + 1, high + 1
            elif ch == ")":
                low, high = low - 1, high - 1
            else:
                low, high = low - 1, high + 1
            if low < 0:
                low = 0
            if high < 0:
                return False
