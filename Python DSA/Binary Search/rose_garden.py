# Rose Garden - Coding Ninja

# no of rose
n = 9
# days when it blooms
arr = [ 1, 2, 1, 2, 7, 2, 2, 3, 1 ]
# no of roses in bouquet
k = 3
# no of bouquet
m = 2

if k*m > n:
    print(-1)

# checking if all bouquet can be formed
def possible(arr, day, k, m):
    cnt = 0
    total_bouquet = 0
    for i in range(n):
        if arr[i] <= day:
            cnt += 1
        else:
            total_bouquet += cnt//k
            cnt = 0
    total_bouquet += cnt//k
    return total_bouquet >= m 

for i in range(min(arr), max(arr)+1):
    if possible(arr, i, k, m):
        print(i)
        break
print(-1)