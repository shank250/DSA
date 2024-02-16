# 1481. Least Number of Unique Integers after K Removals

arr = [4,3,1,1,3,3,2]
k = 3

# def findLeastNumOfUniqueInts():
#     from collections import Counter
#     hm = Counter(arr)
#     for i in range(len(arr)):
#         if i in hm.values():
#             for key, val in hm.items():
#                 if val == i:
class Solution:
    def findLeastNumOfUniqueInts() -> int:
        from collections import Counter
        freq_map = Counter(arr)

        sorted_freq = sorted(freq_map.items(), key=lambda x: x[1])

        for num, freq in sorted_freq:
            if k >= freq:
                k -= freq
                del freq_map[num]
            else:
                break

        return len(freq_map)