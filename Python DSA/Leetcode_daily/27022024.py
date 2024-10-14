from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    # Approach 1:
        # To solve this question i will create one methord which 
        # will return me the max depth in the left and right subtree

        # Then I will check for the max depth values of left and right 
        # subtree and add them and update the max if required

class main:
    def __init__(self) -> None:
        self.root = TreeNode(val=1)
        self.root.left = TreeNode(val=2)
        self.root.right = TreeNode(val=3)
        self.root.left.left = TreeNode(val=4)
        self.root.left.right = TreeNode(val=5)
        self.root.left.right.left = TreeNode(val=6)

    def depthFinder(self, root):
        if root is None:
            return 0
        return 1 + max(self.depthFinder(root=root.left), self.depthFinder(root=root.right))
    
    def diameterOfBinaryTree(self, root) -> int:
        maxDepth = 0
        queue = [root]
        while len(queue):
            node = queue.pop(0)
            Rdepth, Ldepth = 0, 0
            if node.left is not None:
                queue.append(node.left)
                Ldepth = self.depthFinder(node.left)
            if node.right is not None:
                queue.append(node.right)
                Rdepth = self.depthFinder(node.right)
            if (Ldepth + Rdepth) > maxDepth :
                maxDepth = (Ldepth + Rdepth )
        return maxDepth
    
main = main()
num = main.diameterOfBinaryTree(main.root)
print(num)