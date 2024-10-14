# 661. Image Smoother
# like max pooling layer in CNN

img = [[100,200,100],[200,50,200],[100,200,100]]
m, n = len(img), len(img[0])
result = [[0] * n for _ in range(m)]
arr = []
for i, row in enumerate(img):
    for j, ele in enumerate(row):
        total, count = 0, 0
        for x in range(max(0, i - 1), min(m, i + 2)):
            for y in range(max(0, j - 1), min(n, j + 2)):
                total += img[x][y]
                count += 1
        result[i][j] = total // count
print(result)


# # methord 2 with try except block
# def opr(i, j):
#     s, n = 0, 0
#     for x in range(i-1, i+2):
#         for y in range(j-1, j+2):
#             try:
#                 s += img[x][y]
#                 # print(img[x][y])
#                 n += 1
#             except IndexError:
#                 continue
#         # break
#     # print(s//n)
#     # print(s," ",n)
#     return s//n

# rows, cols = len(img), len(img[0])
# new = [[0 for _ in range(cols)] for a in range(rows)]
# for i in range(rows):
#     for j in range(cols):
#         new[i][j] = opr(i, j)
# print(new)