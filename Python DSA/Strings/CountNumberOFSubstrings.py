# Count Number of Substrings

s = "aacfssa"    
k = 3

from collections import Counter

allSubStrings = []
for i in range(maxPossibleIndex := len(s)-k):
    endIndex = i + k
    while endIndex <= len(s):
        allSubStrings.append(s[i:endIndex])
        endIndex += 1
counter = 0

for ele in allSubStrings:
    hm = Counter(ele)
    if len(hm) == k:
        counter += 1
        # print(ele)

print(counter)


# properSubStr = []
# checkLR = []

# for i in range(len(s)-k):
#     if len(Counter(s[i:i+k])) == k:
#         properSubStr.append(s[i:i+k])
#         checkLR.append(s[i:i+k])

# def recheckLR():
#     global properSubStr
#     print(properSubStr)
#     global checkLR
#     if len(checkLR) != 0:
#         targetStr  = checkLR[0]
#     else:
#         return properSubStr
#     for ch in targetStr:
#         lstr = ch + targetStr
#         rstr = targetStr + ch

#         if lstr in s:
#             checkLR.append(lstr)
#             properSubStr.append(lstr)
#         if rstr in s:
#             checkLR.append(rstr)    
#             properSubStr.append(rstr)

#     checkLR.remove(targetStr)
#     recheckLR()

# print(recheckLR())
# # Code not working yet :P  

