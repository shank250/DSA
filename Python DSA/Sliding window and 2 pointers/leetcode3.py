# Longest Substring Without Repeating Characters

s = "abcabcbb"

from collections import Counter

def checkDuplicates(s):
    '''returns true is thier is any duplicate in str'''
    hmp = Counter(s)
    for val in hmp.values():
        if val > 1:
            return True
    return False

def maxSubstring(s):
    windowSize = len(list(s))

    while windowSize:

        start = 0
        end = start + windowSize
        while end <= len(list(s)):

            target = s[start:end]
            if not checkDuplicates(target):
                return windowSize
            start += 1

        windowSize -= 1
    return windowSize

print(maxSubstring(s))