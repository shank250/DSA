package JavaDSA.MockInterview;
import java.util.*;

class RightViewBinaryTree{
    public static List<Integer> rightView(Node head){
        if(head == null)
            return new ArrayList<Integer>();
        
        Queue<Pair> queue = new LinkedList<>();
        queue.offer(new Pair(head, 0));
        List<Integer> ans = new ArrayList<>();
        int lastVal = head.val;
        int lastLevel = 0;
        int leterallyLastVal = head.val;

        while (queue.size() != 0) {
            Pair pair = queue.poll();
            Node node = pair.node;

            if(node.left != null)
                queue.offer(new Pair(node.left, lastLevel + 1));

            if(node.right != null) 
                queue.offer(new Pair(node.right, lastLevel + 1));

            if(pair.level == lastLevel){
                lastVal = node.val;  
            }else{
                ans.add(lastVal);
                lastLevel = pair.level;
            }

            leterallyLastVal = node.val;
        }
        ans.add(leterallyLastVal);
        return ans;
    }

    public static void main(String[] args) {
        Node head = new Node(2);
        head.left = new Node(1);
        head.right = new Node(3);
        head.left.left = new Node(4);

        List<Integer> ans = rightView(head);
        ans.forEach(System.out::print);
    }

}

class Node{
    int val;
    Node left;
    Node right;
    Node(int val){
        this.val = val;
    }
}

class Pair{
    Node node;
    int level;
    Pair(Node node,int level){
        this.node = node;
        this.level = level;
    }
}

