# nums = [1,0,-1,0,-2,2]
arr = [1, -1, 0, 0, 1]

sum = 0
maxi = 0
hm = {}
for index, ele in enumerate(arr):
    sum += ele
    if sum == 0:
        maxi = index + 1
    else:
        if sum in hm:
            maxi = max(maxi, index - hm[sum])
        else:
            hm[sum] = index
print(maxi)