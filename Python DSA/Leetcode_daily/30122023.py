# dont retrun easy question

# class Solution:
#     def makeEqual(self, words: List[str]) -> bool:
words = ["abc","aabc","bc"]
noOfWords = len(words)
hashing = {}
word = "".join(words)
for ch in word:
    if ch in hashing:
        hashing[ch] += 1
    else:
        hashing[ch] = 1
print(all(value % noOfWords == 0 for value in hashing.values()))
