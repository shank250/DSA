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