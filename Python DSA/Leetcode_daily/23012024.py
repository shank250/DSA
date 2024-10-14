# 1239. Maximum Length of a Concatenated String with Unique Characters

arr = ["un","iq","ule"]
set_list = []
for ele in arr:
    s = set()
    for ch in ele:
        s.add(ch)
    set_list.append(s)
print(set_list)
import os
os.