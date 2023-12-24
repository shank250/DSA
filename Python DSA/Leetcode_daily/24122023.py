# 1758. Minimum Changes To Make Alternating Binary String
# Easy
# Topics
# Companies
# Hint

# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

# Return the minimum number of operations needed to make s alternating.

s = "0100"
prev = s[0]
rtn = 0
# check the frist number
# then check the wheather the next number is same or not
# if its same then increase the rtn value
# and update the prev with the value it should be
# further on if its different then dont change and update the rtn value
for i, current in enumerate(s):
    if i == 0:
        pass
    else:
        if prev == current:
            rtn += 1
            if prev == "0":
                prev = "1"
            else:
                prev = "0"
        else:
            if prev == "0":
                prev = "1"
            else:
                prev = "0"
print(rtn)
