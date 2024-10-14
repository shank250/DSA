package Tree;

import java.util.*;

class Q103 {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        Stack<TreeNode> stack1 = new Stack<>();
        Stack<TreeNode> stack2 = new Stack<>();
        
        List<List<Integer>> ans = new ArrayList<>();
        
        if(root != null) stack1.add(root);
        else return ans;
        
        while(stack1.size() != 0 || stack2.size() != 0){
            if(stack1.size() != 0){
                List<Integer> interAns = new ArrayList<>();
                while(stack1.size() != 0){
                    TreeNode node = stack1.pop();
                    interAns.add(node.val);
                    if(node.left != null) stack2.push(node.left);
                    if(node.right != null) stack2.push(node.right);
                }
                ans.add(interAns);
            }
            else{
                List<Integer> interAns = new ArrayList<>();
                while(stack2.size() != 0){
                    TreeNode node = stack2.pop();
                    interAns.add(node.val);
                    if(node.right != null) stack1.push(node.right);
                    if(node.left != null) stack1.push(node.left);
                }
                ans.add(interAns);
            }
        }
        
        return ans;
    }
}