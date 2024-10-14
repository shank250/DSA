# Check If One String Is A Rotation Of Another String
p = "abac"
q = "baqa"
p = str(p)+str(p)
index = p.find(q)
print(index)