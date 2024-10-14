arr = [2,3,5,7]
max1, max2 = arr[0], arr[1]
for i in range(len(arr) - 1):
    if arr[i] > max1:
        max2 = max1
        max1 = arr[i]
