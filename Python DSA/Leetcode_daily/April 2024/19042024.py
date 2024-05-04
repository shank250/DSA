grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","1","0"]
]

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited, rtn = set(), 0
        def checkSurrounding(x, y):
            isILand = 0
            if (x, y) not in visited:
                toBeVisited =[(x, y)]
                while toBeVisited := list(set(toBeVisited) - set(visited)):
                    x, y = toBeVisited.pop()
                    visited.add((x, y))
                    if (x - 1) >= 0: 
                        if grid[y][x - 1] == "1" and ((x - 1, y) not in visited): toBeVisited.append((x - 1, y))
                           
                    if (y - 1) >= 0:
                        if grid[y - 1][x] == "1" and ((x , y - 1) not in visited): toBeVisited.append((x, y - 1))
                           
                    if (x + 1) < cols:
                        if grid[y][x + 1] == "1" and ((x + 1, y) not in visited): toBeVisited.append((x + 1, y))
                           
                    if (y + 1) < rows:
                        if grid[y + 1][x] == "1" and ((x , y + 1) not in visited): toBeVisited.append((x, y + 1))

                isILand = 1
            return isILand
        for y in range(rows):
            for x in range(cols):
                if (x, y) not in visited:
                    if grid[y][x] == "1":
                        isLand = checkSurrounding(x, y)
                        rtn += isLand
        print(rtn)
        return rtn
sol = Solution().numIslands(grid)