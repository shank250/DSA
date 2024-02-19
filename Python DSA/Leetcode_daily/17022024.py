# 1642. Furthest Building You Can Reach

heights = [1, 2]
bricks = 0
ladders = 0
def furthestBuilding():
    difHeight = []
    for i in range(len(heights)-1):
        if (heights[i+1] - heights[i]) > 0:
            difHeight.append(heights[i+1] - heights[i])
        else:
            difHeight.append(0)
    val = sum(x for x in difHeight if x != 0) 
    print(val)
    if val == 0 :
        return len(heights)
    # reversed iteration
    for index, element in enumerate(reversed(difHeight)):
        splitedDifHeight = difHeight[:len(difHeight)-index]
        # print(splitedDifHeight)
        for ietrations in range(ladders):
            val = max(splitedDifHeight)
            splitedDifHeight.reverse()
            splitedDifHeight.remove(val)
            splitedDifHeight.reverse()
            # print(splitedDifHeight)
        heightDifSum = sum(splitedDifHeight)
        if heightDifSum <= bricks:
            return len(difHeight) - index

print(furthestBuilding())