# Sum between low and high in BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: [TreeNode], low: int, high: int) -> int:
        def findingsum(node):
            if not node:
                return 0
            
            current_val = 0
            if low <= node.val <= high:
                current_val = node.val
            
            left_sum = findingsum(node.left)
            right_sum = findingsum(node.right)
            
            return current_val + left_sum + right_sum

        return findingsum(root)