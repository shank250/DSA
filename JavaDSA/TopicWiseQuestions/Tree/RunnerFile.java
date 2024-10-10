package JavaDSA.TopicWiseQuestions.Tree;


import java.util.ArrayList;
import java.util.List;
// import javax.swing.tree.MyTreeNode;

// DSA.TopicWiseQuestions.Tree;

public class RunnerFile {
    public static void main(String[] args) {
        MyTreeNode root = new MyTreeNode(1);
        root.left = new MyTreeNode(2);
        root.right = new MyTreeNode(3);
        root.left.left = new MyTreeNode(4);
        root.right.left = new MyTreeNode(5);
        root.right.left.right = new MyTreeNode(6);
        MorrisTraversal traversal = new MorrisTraversal();
        List<Integer> list = new ArrayList<>();
        traversal.inorder(root, list);
        list.forEach(System.out::print);
    }
}
