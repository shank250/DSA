# 1436. Destination City

# output = A

# mine approch

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

# optimal approach
def destCity(paths):
    outgoing_cities = set()
    all_cities = set()

    # Iterate through paths and record outgoing cities
    for path in paths:
        outgoing_cities.add(path[0])
        all_cities.add(path[0])
        all_cities.add(path[1])

    # Find the destination city by finding the city without outgoing path
    destination_city = (all_cities - outgoing_cities).pop()

    return destination_city