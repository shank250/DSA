# 2971. Find Polygon With the Largest Perimeter

nums = [5, 5, 5]
def largestPerimeter():
    sum_ = sum(nums)
    nums.sort()
    # print(sum_)
    dif = 0
    for i in range(len(nums)-1, 0, -1):
        print("iteration : ",nums[i])
        if ((sum_- (nums[i] + dif)) > nums[i]) and (i >= 2):
            return sum_ - dif
        else:
            dif = dif +  nums[i]
            print("dif : ", dif)
    return -1

print(largestPerimeter())