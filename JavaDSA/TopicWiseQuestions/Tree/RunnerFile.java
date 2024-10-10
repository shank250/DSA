package JavaDSA.TopicWiseQuestions.Tree;


import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
// import javax.swing.tree.MyTreeNode;
import java.util.Scanner;
import java.util.LinkedList;
// DSA.TopicWiseQuestions.Tree;

public class RunnerFile {
    public  void dfs(MyTreeNode root){
        if(root == null) return;

        dfs(root.left);
        System.out.println(root.data);
        dfs(root.right);
        
        return;
    }


    public static void main(String[] args) {
        // MyTreeNode root = new MyTreeNode(1);
        // root.left = new MyTreeNode(2);
        // root.right = new MyTreeNode(3);
        // root.left.left = new MyTreeNode(4);
        // root.right.left = new MyTreeNode(5);
        // root.right.left.right = new MyTreeNode(6);
        // MorrisTraversal traversal = new MorrisTraversal();
        // args.forEach(System.out::print);
        // for(String st : args){
        //     System.out.println(st);
        // }
        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();
        // String input = args[1];
        String[] listinp = input.split(" ");
        Queue<MyTreeNode> queue = new LinkedList<MyTreeNode>();

        if(listinp.length == 0){
            System.out.println("No input found!");
            return;
        }

        MyTreeNode root = new MyTreeNode(Integer.parseInt(listinp[0])); // axxuming the first node value is in int
        queue.offer(root);
        MyTreeNode temp = root;
        // take two consicutive elements from the listint and then 
        // map each of them to the head of the queue(use poll) and then
        //  add the newly created nodes to the queue
        int ind = 1, limit = listinp.length;
        while(ind < limit){
            MyTreeNode oldNode = queue.poll();

            if(!listinp[ind].equals("null")){
                MyTreeNode newNodeLeft = new MyTreeNode(Integer.parseInt(listinp[ind]));
                oldNode.left = newNodeLeft;
                queue.offer(newNodeLeft);
            }
            ind++;
            if(ind < limit && !listinp[ind].equals("null")){
                MyTreeNode newNodeRight = new MyTreeNode(Integer.parseInt(listinp[ind]));
                oldNode.right = newNodeRight;
                queue.offer(newNodeRight);
            }
            ind++;
        } 
        // RunnerFile run =  new RunnerFile();

        // run.dfs(temp);
        List<Integer> list = new ArrayList<>();
        MorrisTraversal traversal = new MorrisTraversal();
        list = traversal.inorder(temp, list);
        list.forEach(System.out::print);



    }
}
