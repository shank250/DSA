
def rowWithMax1s(matrix: [[int]], n: int, m: int) -> int:
    maxCount = 0
    ans = -1

    for i in range(n):
        curr = 0
        for j in range(m):
            if matrix[i][j] == 1:
                curr += 1
        if curr > maxCount:
            ans = i
            maxCount = curr

    return ans