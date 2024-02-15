# 1291. Sequential Digits
low = 100
high = 300

# low_ele = []
# for ele in str(low):
#     low_ele.append(ele)

# begin = []
# initial = int(low_ele[0])

def initialAndSteps(num):
    steps = 1
    while num > 9:
        num = num // 10
        steps += 1
    return num, steps


def numCreator(init, steps):
    result = 0
    for i in range(steps):
        result += init*(10**(steps-1-i))
        init += 1
    return result

rtn = []
# beg = numCreator(initial, len(low_ele))
# if beg < low:
#     print( rtn)

# while beg < high:
while low < high:
    newNum = numCreator(initialAndSteps(low))

    if newNum < low:
        pass
    else:
        if newNum <= high:
            rtn.append(newNum)
    




