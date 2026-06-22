from math import gcd
 
test_cases = int(input())
 
for _ in range(test_cases):
    n = int(input())
    nums = list(map(int, input().split()))
    
    gcd_pre = [nums[0] for n in nums]
    gcd_suf = [nums[-1] for n in nums]
    
    for i in range(n - 1):
        gcd_pre[i + 1] = gcd(gcd_pre[i], nums[i + 1])
        gcd_suf[n - i - 2] = gcd(gcd_suf[n - i - 1], nums[n - i - 2])
 
    found_ans = False
    
    for i in range(n - 1):
        if gcd_pre[i] != gcd_suf[i + 1]:
            ans = [1 if x <= i else 2 for x in range(n)]
            found_ans = True
            break
    
    if found_ans:
        print("Yes")
        print(" ".join(map(str, ans)))
    else:
        print("No")