
# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence

# 872. Leaf-Similar Trees
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: [TreeNode], root2: [TreeNode]) -> bool:
        set1 = []
        set2 = []
        def traverse(root, settmp):         
            if root.left == None and root.right == None:
                settmp.append(root.val)
            if root.left != None:
                traverse(root.left, settmp)
            if root.right != None:
                traverse(root.right, settmp)
            return settmp
        set1 = traverse(root1, set1)
        set2 = traverse(root2, set2)
        return set1 == set2
