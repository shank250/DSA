import java.util.*;

import javax.swing.tree.TreeNode;
/*
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int maxPossible(TreeNode root, TreeNode max){
        if(root == null) return 0;

        int left = Math.max(maxPossible(root.left, max), 0);
        int right = Math.max(maxPossible(root.right, max), 0);

        int maxVal = Math.max(left + right + root.val, Math.max(Math.max(left + root.val, right + root.val), root.val));
        if(max.val < maxVal) max.val = maxVal;

        return root.val + Math.max(left, right);
    }
    
    public int maxPathSum(TreeNode root) {
        /*Here i will call the maxPossible function at each of the node.
        which will return me the path of max possible sum.
        we will also update the max Treenode in between this same funciton which will be containing our ans. */    
        TreeNode ans = new TreeNode();
        ans.val = Integer.MIN_VALUE;
        int possibleAns = maxPossible(root, ans);
        return ans.val == Integer.MIN_VALUE ? possibleAns : ans.val;
    }
}