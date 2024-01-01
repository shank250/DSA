# 1624. Largest Substring Between Two Equal Characters
# Solved
# Easy
# Topics
# Companies
# Hint

# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

# A substring is a contiguous sequence of characters within a string.

s = "abca"
hashing = {}
maxVal = -1
for index, i in enumerate(s):
    if i in hashing:
        if (index - hashing[i]) > maxVal:
            maxVal = (index - hashing[i])
    else:
        hashing[i] = index
# if maxVal == -1:
    # return -1
# else:
    # return maxVal-1