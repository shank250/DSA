# # dont retrun easy question

# # class Solution:
# #     def makeEqual(self, words: List[str]) -> bool:
# words = ["abc","aabc","bc"]
# noOfWords = len(words)
# hashing = {}
# word = "".join(words)
# for ch in word:
#     if ch in hashing:
#         hashing[ch] += 1
#     else:
#         hashing[ch] = 1
# print(all(value % noOfWords == 0 for value in hashing.values()))
rtn = []
stack = [1,2,3]
for i in range(len(stack), 0 , -1):
    val = stack[i-1]
    rtn.append(val)
# return rtn
print(rtn)