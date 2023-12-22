ll = [1,2,3,4,5]
n=5
k=2
def fnswap(start, end):
    dif = end - start
    iterat = dif // 2
    for i in range(iterat):
        tmp = ll[end-1-i]
        ll[end - i -1] = ll[start + i]
        ll[start + i] = tmp 
    return ll
    # M1 swap function which swaps the values
numOfTimes = len(ll)//k
start = 0
for i in range(numOfTimes):
    ll = fnswap(start, start + k)
    start = start + k
print(ll)