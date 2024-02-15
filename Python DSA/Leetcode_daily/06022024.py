# 49. Group Anagrams

strs = ["eat","tea","tan","ate","nat","bat"]

from collections import Counter

result = []
dictResult = []

for word in strs:
    hm = Counter(word)
    if hm in dictResult:
        index = dictResult.index(hm)
        result[index].append(word)
    else:
        # append the words and its hm
        result.append([word])
        dictResult.append(hm)
    
print(result)
        