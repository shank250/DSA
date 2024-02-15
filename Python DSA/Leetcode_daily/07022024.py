class Solution:
    def frequencySort(self, s: str) -> str:
        n = 0
        hash = {}
        for i in s:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
            n += 1
        for i in range(n):
            sorted_dic_desending_order = sorted(hash.items(), key= lambda item: item[1], reverse=True)
        rtn = []
        for j in sorted_dic_desending_order:
            for k in range(j[1]):
                rtn.append(j[0])
        return ''.join(rtn)
    