# 513. Find Bottom Left Tree Value

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.root = TreeNode(10)
        self.root.left = TreeNode(5)
        self.root.right = TreeNode(15)
        # self.root.left.left = TreeNode(4)
        self.root.right.left = TreeNode(6)
        self.root.right.right = TreeNode(20)
        # self.root.right.left.left = TreeNode(7)
# [10,5,15,null,null,6,20]
        self.traverseQueue = [self.root]
        self.isLeft = [True]
        self.botttomLeft = self.root.val

        self.node = []
        self.level = []
        self.level = 0
        
# Approach 1 : Failed
    # Take 2 queues, one for traversing and another for keeping count of the 
    # current nodes position is left child or not
# Approach 2 : 
    # Take a recursive function with node, its level, and a bool type variable 
    # for detecting if its left child or not
        
    def travel(self, node, level, isleftChild = True):
        if (node.left == None) and (node.right == None):    
            self.node.append(node.val)
            self.level.append(level)

        if node.left != None:
            self.travel(node.left, level + 1, True)
        if node.right != None:
            self.travel(node.right, level + 1, False)

    def findBottomLeftValue(self):
        
        self.travel(self.root, self.level)
        val = self.root.val
        print(self.nodeAndlevel)

        maxLevel = max(self.level)
        index = self.level.index(maxLevel)
        return self.node[index]


        # prevLevel = self.nodeAndlevel[-1][0]
        # for index, ele in enumerate(reversed(self.nodeAndlevel)):
        #     if ele[0] == prevLevel:
        #         pass
        #     else:
        #         break
        # lenght = len(self.nodeAndlevel)
        # req = self.nodeAndlevel[lenght-index-1:]
        # # print(req)
        # return req[0][1]
        # while len(self.traverseQueue):
        #     node = self.traverseQueue.pop(0)
        #     isItLeft = self.isLeft.pop(0)

        #     if (node.left == None) and (node.right == None):
        #         if isItLeft:
        #             self.botttomLeft = node.val
        #     if  (node.left != None):
        #         self.traverseQueue.append(node.left)
        #         self.isLeft.append(True)
        #     if (node.right != None):
        #         self.traverseQueue.append(node.right)
        #         self.isLeft.append(False)

        # return self.botttomLeft

sol = Solution().findBottomLeftValue()
print(sol)