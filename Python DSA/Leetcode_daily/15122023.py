# 1436. Destination City

# output = A

# approch
# iterate n time(may be even this is not required)
# take element paths[0][1] and search this anywhere at the path[i][0]
# if you get that element then again take paths[i][i] and search this
# untill you didnt get that
paths = [["qMTSlfgZlC","ePvzZaqLXj"],
         ["xKhZXfuBeC","TtnllZpKKg"],
         ["ePvzZaqLXj","sxrvXFcqgG"],
         ["sxrvXFcqgG","xKhZXfuBeC"],
         ["TtnllZpKKg","OAxMijOZgW"]]
nRoutes = len(paths)
rtn = []
des = paths[0][1]
def searchDestination(des):
    # global des
    for i in range(nRoutes):
        if des == paths[i][0]:
            des = paths[i][1]
            searchDestination(des)
    # return des

    rtn.append(des)
ans = searchDestination(des)
print(rtn)
