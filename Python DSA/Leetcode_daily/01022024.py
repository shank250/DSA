# Divide Array Into Arrays With Max Difference
nums = [1,3,3,2,7,3]
k = 3
nums.sort()
difList = []
for i in range(len(nums)-1):
    dif = nums[i+1] - nums[i]
    difList.append(dif)
if difList[0] <= k and difList[-1] <= k:
    index = []
    for i in range(1,len(difList)-1,1):
        if difList[i] > k:
            index.append(i)
    if len(index)>2:
        print("impossible")
else:
    print("impossible")

if len(index) == 2:
    pass
elif len(index) == 1:
    start = 0
    end = len(nums)
    mid = index[0]
    