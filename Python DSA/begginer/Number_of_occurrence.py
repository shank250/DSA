# Number of occurrence 
# find the frequency of any number
#  with time complexity of log(n) 

# n = 7 
# x = 3
# arr = [1, 1, 1, 2, 2, 3, 3]
n = 15 
x = 10
arr = [2, 4, 10, 10, 10, 10, 10, 10, 11, 12, 14, 14, 17, 19, 19] 

low, high = 0, n-1
def testOccurence(mid):
    tmid = mid
    print("yes")
    while True:
        if arr[mid] == x:
            mid -= 1
        else:
            start = mid + 1
            break
    mid = tmid
    while True:
        if arr[mid] == x and (mid<n):
            mid+=1
        else:
            end = mid - 1
            print("yess")
            break
    return end-start
while low<=high :
    mid = (low+high)//2
    if arr[mid] == x:
        ans = testOccurence(mid)
        break
    elif arr[mid] > x:
        high = mid - 1
    elif arr[mid] < x:
        low = mid + 1
if ans < 0 :
    print( abs(ans))
else:
    print( abs(ans+1))
print(ans)