# 5. Longest Palindromic Substring

s = "babababd"

def slidingWindow():
    # 3 step sw
    # 2 step sw
    # apend intial index and step size
    initialIndexList = []
    palindromSize = []
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            initialIndexList.append(i)
            palindromSize.append(3)
    for i in range(len(s)-2):
        if s[i] == s[i+1]:
            initialIndexList.append(i)
            palindromSize.append(2)
    print(palindromSize)
    # for index, initiateIndex in enumerate(initialIndexList):
        # stepSize = 1
        # finalStepSize = 0
        # while True:
        #     if  ((initiateIndex + palindromSize[index] + stepSize -1) < len(s)) and ((initiateIndex - stepSize) >= 0) : 
        #         print("running")   
        #         if s[initiateIndex - stepSize] == s[initiateIndex + palindromSize[index] + stepSize - 1]:
        #             finalStepSize = stepSize + 1
        #             stepSize += 1
        #         else:
        #             break
        #     else:
        #         break
        # oldWindowSize = palindromSize[index]
        # palindromSize[index] = finalStepSize + oldWindowSize

    # for index, initsialIndex in enumerate(initialIndexList):
    #     def check(initial=initsialIndex, final=(initsialIndex + palindromSize[index] + ))

    print(palindromSize)

print(slidingWindow())

    
    