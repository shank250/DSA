import javax.swing.tree.TreeNode;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

 class Solution {
    private boolean eitherPQ(TreeNode root, TreeNode p, TreeNode q, TreeNode ans){
        if(root.val == p.val || root.val == q.val) return true;
        if(eitherPQ(root.left, p, q, ans) && eitherPQ(root.right, p, q, ans))
            ans = root;
        return true;
    }

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode ans = new TreeNode(-1);

        boolean found = eitherPQ(root, p, q, ans);
        if(!found) return root;
        return ans
    }
}