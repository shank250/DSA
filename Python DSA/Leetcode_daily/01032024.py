# 2864. Maximum Odd Binary Number

from collections import Counter

s = "0101"

hm = Counter(s)
# 0 times 1 or 1 times 1
front = hm[1] - 1

rtn = "1"*(hm[1]-1) + "0"*(hm[0]) + "1"

