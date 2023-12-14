def firstAndLastPosition(arr, n, k):
    low, high = 0, n-1
    rtn = [-1, -1]
    def gotK(mid):
        while True:
            
            if mid >= 0:
                if arr[mid] != k:
                    rtn[0] = mid + 1
                    break
            else:
                rtn[0] = mid + 1
            mid -= 1
        while True:
            mid += 1
            if mid < n:
                if arr[mid] != k:
                    rtn[1] = mid - 1
                    break
            else:
                rtn[1] = mid - 1
                break
        print(rtn)
        return rtn
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == k:
            gotK(mid)
            break
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    rtn = [-1,-1]
    return rtn
arr = [5,7,7,8,8,10]
n = 6
k = 8
firstAndLastPosition(arr, n, k)