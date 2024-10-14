# class Solution:
#     def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
def onesMinusZeros(grid):
    n, m = len(grid), len(grid[0])
    listcntColm = [[0, 0] for i in range(m)]
    listcntRown = [[0, 0] for i in range(n)]
    rtn = [[0 for i in range(m)] for j in range(n)]
    for y in range(m):
        cnt1, cnt0 = 0, 0
        for x in range(n):
            if grid[x][y] == 0:
                cnt0 += 1
            elif grid[x][y] == 1:
                cnt1 += 1
        listcntColm[y][0] = cnt0
        listcntColm[y][1] = cnt1

    for x in range(n):
        cnt1, cnt0 = 0, 0
        for y in range(m):
            if grid[x][y] == 0:
                cnt0 += 1
            elif grid[x][y] == 1:
                cnt1 += 1
        listcntRown[x][0] = cnt0
        listcntRown[x][1] = cnt1
    
    for y in range(m):
        for x in range(n):
            rtn[x][y] = listcntColm[y][1] + listcntRown[x][1] - (listcntColm[y][0] + listcntRown[x][0])
    print(rtn)
    return rtn
grid = [[1,1,1],[1,1,1]]
onesMinusZeros(grid)