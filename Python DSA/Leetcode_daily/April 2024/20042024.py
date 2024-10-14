# 1992. Find All Groups of Farmland
land = [[1,0,0],[0,1,1],[0,1,1]]

class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        pairs = []
        rows, cols = len(land), len(land[0])
        def dfs(x, y, xMax, yMax):
            if 0 <= x < cols and 0 <= y < rows and land[y][x] == 1:
                land[y][x] = 0
                xMax = max(x, xMax)
                yMax = min(y, yMax)
                letx, lety = dfs(x + 1, y, xMax, yMax)
                yMax, xMax = max(yMax, lety), max(xMax, letx)
                letx, lety = dfs(x, y + 1, xMax, yMax)
                yMax, xMax = max(yMax, lety), max(xMax, letx)
                letx, lety = dfs(x - 1, y, xMax, yMax)
                yMax, xMax = max(yMax, lety), max(xMax, letx)
                letx, lety = dfs(x, y - 1, xMax, yMax)
                yMax, xMax = max(yMax, lety), max(xMax, letx)
                # dfs(x + 1, y, xMax, yMax)
                # dfs(x, y + 1, xMax, yMax)
                # dfs(x - 1, y, xMax, yMax)
                # dfs(x, y - 1, xMax, yMax)
                return xMax, yMax
            return -1, -1

        for y in range(rows):
            for x in range(cols):
                if land[y][x] == 1:
                    xMax, yMax = dfs(x, y, x, y)
                    pairs.append([x, y, xMax, yMax])
        print(pairs)
        return pairs
sol = Solution().findFarmland(land)