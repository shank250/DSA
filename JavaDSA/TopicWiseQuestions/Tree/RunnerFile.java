package Tree;

import java.util.*;


public class RunnerFile {
    public  void dfs(TreeNode root){
        if(root == null) return;

        dfs(root.left);
        System.out.println(root.val);
        dfs(root.right);
        
        return;
    }

    public static void main(String[] args) {
        // TreeNode root = new TreeNode(1);
        // root.left = new TreeNode(2);
        // root.right = new TreeNode(3);
        // root.left.left = new TreeNode(4);
        // root.right.left = new TreeNode(5);
        // root.right.left.right = new TreeNode(6);
        // MorrisTraversal traversal = new MorrisTraversal();
        // args.forEach(System.out::print);
        // for(String st : args){
        //     System.out.println(st);
        // }
        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();
        // String input = args[1];
        String[] listinp = input.split(" ");
        Queue<TreeNode> queue = new LinkedList<TreeNode>();

        if(listinp.length == 0){
            System.out.println("No input found!");
            return;
        }

        TreeNode root = new TreeNode(Integer.parseInt(listinp[0])); // axxuming the first node value is in int
        queue.offer(root);
        TreeNode temp = root;
        // take two consicutive elements from the listint and then 
        // map each of them to the head of the queue(use poll) and then
        //  add the newly created nodes to the queue
        int ind = 1, limit = listinp.length;
        while(ind < limit){
            TreeNode oldNode = queue.poll();

            if(!listinp[ind].equals("null")){
                TreeNode newNodeLeft = new TreeNode(Integer.parseInt(listinp[ind]));
                oldNode.left = newNodeLeft;
                queue.offer(newNodeLeft);
            }
            ind++;
            if(ind < limit && !listinp[ind].equals("null")){
                TreeNode newNodeRight = new TreeNode(Integer.parseInt(listinp[ind]));
                oldNode.right = newNodeRight;
                queue.offer(newNodeRight);
            }
            ind++;
        } 

        // List<Integer> list = new ArrayList<>();
        // MorrisTraversal traversal = new MorrisTraversal();
        // list = traversal.inorder(temp, list);
        // list.forEach(System.out::print);

        Q103 que = new Q103();
        List<List<Integer>> ans  =  que.zigzagLevelOrder(temp);
        ans.forEach(System.out::print);


    }
}
