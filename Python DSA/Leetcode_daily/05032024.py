# 1750. Minimum Length of String After Deleting Similar Ends

s = "aabccabba"

class Solution:
    def minimumLength(self, s: str) -> int:
        s = list(s)

        while len(s) > 1:
            if s[0] == s[-1]:
                currentChar = s[0]
                while s[0] == currentChar:
                    s.pop(0)
                while s[-1] == currentChar:
                    s.pop(-1)
            else:
                break
        return len(s)
print(Solution().minimumLength(s))