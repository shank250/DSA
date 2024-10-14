# 513. Even Odd Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict
class Solution:
    def __init__(self) -> None:
        self.root = TreeNode(1)
        self.root.left = TreeNode(10)
        self.root.right = TreeNode(1)
        self.root.left.left = TreeNode(3)
        self.root.right.left = TreeNode(7)
        self.root.right.right = TreeNode(11)
        self.root.right.left.left = TreeNode(20)


    def isEvenOddTree(self, root):
        self.levelWiseElements = defaultdict(list)
        def traverse(node, level):
            if node is None:
                return
            val = node.val
            if val != None:
                self.levelWiseElements[level].append(val)
            if node.left != None:
                traverse(node.left, level + 1)
            if node.right != None:
                traverse(node.right, level + 1)
        traverse(root, 0)
        def is_sorted(data):
            if len(data) <= 1:
                return True
            for i in range(len(data) - 1):
                if data[i] >= data[i + 1]:
                    return False
            return True
        
        def is_odd(data):
            for val in data:
                if (val%2) != 1:
                    return False
            return True
        def is_even(data):
            for val in data:
                if (val%2) != 0:
                    return False
            return True

        for level, values in self.levelWiseElements.items():
            check = False
            if level == 3:
                check = True
            if (level%2) == 0:
                # even levels
                # odd values & accesnding
                if is_odd(values):
                    if is_sorted(values):
                        pass
                    else:
                        return False
                else:
                    return False
            else:
                # odd level
                # even values & decending
                if not is_even(values):
                    reversed_list = list(reversed(values))
                    if is_sorted(reversed_list)  or (len(values)<=1):
                        pass
                    else:
                        return False
                else:
                    return False
        
        return True
sol = Solution()
rtn = sol.isEvenOddTree(sol.root)
print(rtn)