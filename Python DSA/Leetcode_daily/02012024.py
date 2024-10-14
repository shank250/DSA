# 2610. Convert an Array Into a 2D Array With Conditions
# Medium
# Topics
# Companies
# Hint

# You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

#     The 2D array should contain only the elements of the array nums.
#     Each row in the 2D array contains distinct integers.
#     The number of rows in the 2D array should be minimal.

# Return the resulting array. If there are multiple answers, return any of them.

# Note that the 2D array can have a different number of elements on each row.

nums = [1,3,4,1,2,3,1]
hashing = {}
for ele in nums:
    if ele in hashing:
        hashing[ele] += 1
    else:
        hashing[ele] = 1
rtn = []
rows = max(hashing[x] for x in hashing)
for iter in range(rows):
    row = []
    for i, ele in enumerate(nums):
        if hashing[ele] > 0 and ele not in row:
            row.append(ele)
            # nums.pop(i)
            hashing[ele] -= 1
    rtn.append(row)
print(rtn)

