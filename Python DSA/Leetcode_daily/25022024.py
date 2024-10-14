# 2709. Greatest Common Divisor Traversal

from collections import deque, defaultdict

nums = [4,3,12,8]
avalaiblePaths = defaultdict(list)
findPath = []

def isGcdMoreThanOne(i, j):
    max = min(i, j)
    for commonFacror in range(max, 0, -1):
        if ((i % commonFacror) == 0) and ((j % commonFacror) == 0):
            if commonFacror > 1:
                return True
            else:
                return False

def bfs(graph, start, end):
    visited = set()
    # why [ brackets ] ?
    queue = deque([start])

    while queue:
        current = queue.popleft()
        visited.add(current)

        if current == end:
            return True
        
        for neighbor in graph[current]:
            print()
            if neighbor not in visited:
                queue.append(neighbor)

    return False

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if isGcdMoreThanOne(i=nums[i], j=nums[j]):
            avalaiblePaths[i].append(j)
            avalaiblePaths[j].append(i)
        else:
            findPath.append((i, j))

def main():
    for find in findPath:
        i, j =  find
        if bfs(avalaiblePaths, i, j):
            avalaiblePaths[i].append(j)
            avalaiblePaths[j].append(i)
        else:
            print(i,j)
            return False
    return True

print(main())
