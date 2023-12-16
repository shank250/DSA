# leetcode daily question 
#  question is asking to tell if 
#  wheater a new word is made up of
#  the wxisting words character or not

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count_s = {}
    count_t = {}
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1
    print(count_s, count_t)
    return count_s == count_t

s = "rat"
t = "car"
isAnagram(s=s,t=t)