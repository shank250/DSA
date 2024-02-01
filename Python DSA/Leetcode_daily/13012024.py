
# You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.
# Return the minimum number of steps to make t an anagram of s.
# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
# 1347. Minimum Number of Steps to Make Two Strings Anagram
s, t = "leetcode", "practice"
from collections import Counter
makeThis = Counter(s)
fromThis = Counter(t)

changes = 0
a
for key, val in makeThis.items():
    if key in fromThis:
        if (makeThis[key] - fromThis[key]) >= 0:
            changes += makeThis[key] - fromThis[key]
    else:
        changes += makeThis[key]

print(changes)