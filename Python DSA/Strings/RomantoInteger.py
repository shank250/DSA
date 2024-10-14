# 13. Roman to Integer

s = "MCMXCIV"

def romanToInt():
    # make a dictionary for roman to interger
    tresure = {
                "I":1,
                "V": 5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000
                }
    # make a list of conversion
    nums = []
    for ch in s:
        nums.append(tresure[ch])
    # look for indexs where the next number  
    # is graeter that the previouse number 
    for idx in range(len(nums) - 1):
        if (nums[idx] - nums[idx+1]) < 0:
            val = nums[idx]
            nums[idx] = - val
    # swap these values with the original values 
    # return the sum
    return sum(nums)

print(romanToInt())
