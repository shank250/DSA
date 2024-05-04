# 930. Binary Subarrays With Sum

nums = [1,0,1,0,1]
goal = 2

# go till the end of the list
length = len(nums)
i, j = 0, 1
# strat with i = 0, j=1
counter = 0
while True:
    # print(i, j)
    _sum = sum(nums[i:j])

    print(nums[i:j])
    if goal == _sum:
        j += 1
        print("yo")
        counter += 1

# then if goal equals to sum increase the j 
    else:
# else check the difference between i and j
        dif = j - i
# if the difference in less then 2 then increase the j
        if dif == 1:
            if j == length:
            # also check if j reaches its outer bound 
            #  if it does reaches then increase i
            # untill i reached second last
                # break the loop
                break
            j += 1
        else:
        # else increse i
            i += 1

print(counter)


