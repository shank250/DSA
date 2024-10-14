# 455. Assign Cookies
# Solved
# Easy
# Topics
# Companies

# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

 

# Example 1:

g = [1,2,3]
s = [1,1]


# class Solution:
    # def findContentChildren(self, g: List[int], s: List[int]) -> int:

no_cookies = len(s)
s.sort()
g.sort()
rtn, counter = 0, 0
for no_child, gf_child in enumerate(g):
    while counter < no_cookies:
        if gf_child <= s[counter]:
            rtn += 1
            counter += 1
            break
        counter += 1
# return rtn