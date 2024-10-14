# def solution(a, b):
#     n = len(a)
#     ans = 0
#     def check(i, j):
#         return a[i] - b[j] == a[j] - b[i]
#     for j in range(n):
#         for i in range(n):
#             if check(i, j): ans += 1
#     return ans
# def solution(a, b):
#     count = 0
#     n = len(a)
    
#     for i in range(n):
#         for j in range(i, n):
#             if a[i] - b[j] == a[j] - b[i]:
#                 count += 1
    
#     return count

from collections import defaultdict
from collections import defaultdict

def solution(a, b):
    count = 0
    n = len(a)
    diff_map = defaultdict(int)
    
    # First pass: count differences
    for i in range(n):
        diff = a[i] - b[i]
        diff_map[diff] += 1
    
    # Second pass: calculate pairs
    for i in range(n):
        diff = a[i] - b[i]
        count += diff_map[diff]  # Include (i,i) pair
        
        # Remove the contribution of (i,i) pair
        if diff_map[diff] > 0:
            diff_map[diff] -= 1
    
    return count

# Test the function
# a = [2, -2, 5, 3]
# b = [1, 5, -1, 1]
# result = solution(a, b)
# print(result)  # Expected output: 6
print(solution([2, -2, 5, 3], [1, 5, -1, 1]))