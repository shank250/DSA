n = 3

# ans = []
nums =  [11,13,31]

# string = string_data.split("0b")
ans = []
for n in nums:
    string = str(bin(n)[2:])
    _list = list(string)
    print(string)
    size = len(_list)
    if n == 2:
        ans.append(-1)
    elif not "0" in _list:
        print("no")
        _list.pop()
        ans.append(int(str("".join(_list)),2))
    elif size >= 2 and _list[-2] == "0":
        _list[-1] = "0"
        ans.append(int(str("".join(_list)),2))
    else:
        
        ptr = size - 1
        count = 0
        ind = -1
        while(ptr):
            if _list[ptr] == "1":
                count+=1
                ptr-=1
            else:
                ind = ptr + 1
                break
        if ind != -1 : 
            _list[ind] = "0"
            ans.append(int(str("".join(_list)),2))
        else:
            ans.append(-1)

print(ans)
