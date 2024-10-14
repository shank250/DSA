hash = {"shashank": 1, "nope": 2, "sam": 3, "ok": 4}
sorted_dic_desending_order = sorted(hash.items(), key= lambda item: item[1], reverse=True)
print(sorted_dic_desending_order)
print(hash.items())