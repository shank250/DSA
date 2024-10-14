# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root) -> int:
        string = []
        def traverse(node, string):
            string.append(str(node.val))
            if not node.left and not node.right:
                num = int("".join(string))
                print(num)
                return num

            if node.left: l = traverse(node.left, string)
            else: l = 0
            if node.right: r = traverse(node.right, string)
            else: r = 0
            return l + r
        return traverse(root, string)

treeRoot = TreeNode()
treeRoot.val = 1

treeRoot.left = treeRoot()
treeRoot.left.val = 2
treeRoot.right = treeRoot()
treeRoot.right.val = 3
sol = Solution().sumNumbers(treeRoot)
