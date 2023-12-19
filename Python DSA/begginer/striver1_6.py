# arr = [ 4, 5, 1, 2, 1,2]
# n = 6


m = 4
arr = [1, 3, 4, 3, 4, 1, 5,2,5,7]
n = len(arr)

# hash = [0 for i in range(1,10)]
# for i in arr:
#     index = int(i) -1
#     hash[index] += 1
# rtrn = hash[:n]
# print(rtrn)


# hash = [0 for i in range(n)]
# for i in arr:
#     index = int(i) -1
#     hash[index] += 1
#     rtrn = hash[:n]
    # return rtrn


#############################################
#2nd approach
# visited = [False for i in range(n)]
# count = 0
# occurance = []
# for index, ele in enumerate(arr):
#     if visited[index] == False :
#         visited[index] = True
#         for index2, ele2 in enumerate(arr):
#             if ele == ele2 and visited[index2] == False :
#                 visited[index2] = True
#                 count += 1
#         occurance.append(count)
#         count = 1
# print(occurance)

# for i in range(1,n+1):
#     for index, ele in enumerate(arr):
#         if ele == i and visited[index] == False:
#             count += 1
#             visited[index] = True
#     occurance.append(count)
#     count = 0
# print(occurance)

###############################################
#3rd Methord
dic = {}
for i in range(n):
    if arr[i] in dic:
        dic[arr[i]] += 1
    else :
        dic[arr
            [i]] = 1
for ele in dic:
    print(ele, dic[ele])


