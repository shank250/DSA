nums = [-1]
tmp = nums.copy()
n = len(tmp)
k = 2

if k > n :
    k = k % n

for i in range(n):
    # if  i >= k then ith value = nums[i - k]
    if i >= k :
        nums[i] = tmp[i - k]
    # else then ith value = nums[- k + i] 
    else :
        nums[i] = tmp[- k + i]
print(nums)
print(tmp)
