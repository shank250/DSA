import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

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
class Pair{
    int left;
    int right;
    Pair(int left, int right){
        this.left = left;
        this.right = right;
    }
}

class Solution {
    private void traversal(int col, TreeNode node, Pair limits, HashMap<Integer,List<Integer>> hm){
        if(node == null) return;

        List<Integer> val = hm.getOrDefault(col, new ArrayList<Integer>());
        val.add(node.val);
        hm.put(col, val);
        
        limits.left = Math.min(limits.left, col);
        limits.right = Math.max(limits.right, col);
        
        this.traversal(col - 1, node.left, limits, hm);
        this.traversal(col + 1, node.right, limits, hm);
        
        return;
    }  
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        /*
         * The plan is to travel the whole bt and add the same column node into the hashmap
         * Then finnaly after the traversal just compile the answer while sorting each of the sub arrays.
         * Also, for getting members from the hashmap we need to know our left to right column.
         *      So, we will store them into the pairs.
         */
        HashMap<Integer,List<Integer>> hm = new HashMap<>();
        List<List<Integer>> ans = new ArrayList<>();
        Pair limits = new Pair();

        this.traversal(0, root, limits, hm);

        for(int i = limits.left; i <= limits.right; i++)
        {
            List<Integer> temp = hm.get(i);
            if (temp != null) {
                temp.sort(null);
            }
            ans.add(temp);
        }
        return ans;
    }
}