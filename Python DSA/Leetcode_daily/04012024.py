# 2870. Minimum Number of Operations to Make Array Empty
# Medium
# Topics
# Companies

# You are given a 0-indexed array nums consisting of positive integers.

# There are two types of operations that you can apply on the array any number of times:

#     Choose two elements with equal values and delete them from the array.
#     Choose three elements with equal values and delete them from the array.

# Return the minimum number of operations required to make the array empty, or -1 if it is not possible.
nums = [2,3,3,2,2,4,2,3,4]
#Failed Algorithum

# ans = 0
# hashmap = {}
# for index, ele in enumerate(nums):
#     if ele in hashmap:
#         hashmap[ele] += 1
#     else:
#         hashmap[ele] = 1
# for ele, val in hashmap.items():
#     if val % 3 == 0:
#         ans += val//3
#     else:
#         if val % 2 == 0:
#             ans += val//2
#         else:
#             print(-1)
#             break

#Learned a new tigdam wali algorithum
# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
from collections import Counter
mp = Counter(nums)

count = 0
for t in mp.values():
    if t == 1:
        # return -1
        print(-1)
    count += t // 3
    if t % 3:
        count += 1
# return count
