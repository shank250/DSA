# 1637. Widest Vertical Area Between Two Points Containing No Points

# Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

# Note that points on the edge of a vertical area are not considered included in the area.

 

# Example 1:
# ​

# Input: points = [[8,7],[9,9],[7,4],[9,7]]
# Output: 1
# Explanation: Both the red and the blue area are optimal.


# class Solution:
#     def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
letsSee = []
rtn = 0
for point in points:
    letsSee.append(point[0])
letsSee.sort()
for i in range(len(letsSee)-1):
    dif = letsSee[i+1] - letsSee[i] 
    if dif >rtn:
        rtn =dif
# return rtn