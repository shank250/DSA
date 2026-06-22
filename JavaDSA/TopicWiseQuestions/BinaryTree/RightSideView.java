import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

import Tree.TreeNode;

/**
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
    public List<Integer> rightSideView(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        List<Integer> ans = new ArrayList<>();

        while(queue.size() != 0){
            int n = queue.size();
            int val = -1;

            while(n-- == 0){
                TreeNode node = queue.poll();
                
                if(node.left != null) queue.offer(node.left);
                if(node.right != null) queue.offer(node.right);

                val = node.val;
            }
            
            ans.add(val);
        }

        return ans;
    }
}