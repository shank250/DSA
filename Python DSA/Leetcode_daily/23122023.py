# 1496. Path Crossing
# Solved
# Easy
# Topics
# Companies
# Hint

# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.


path = "NES"
currentPtr = [0,0]
visited = []
visited.append(currentPtr.copy())
for i in path:
    if i == "N":
        currentPtr[1] += 1
    elif i == "S":
        currentPtr[1] -= 1
    elif i == "E":
        currentPtr[0] += 1
    elif i == "W":
        currentPtr[0] -= 1
    if currentPtr in visited:
        print(True)
    visited.append(currentPtr.copy())
print(False)