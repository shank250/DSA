package JavaDSA.TopicWiseQuestions.Tree;


import java.util.List;

// import javax.swing.tree.MyTreeNode;

// DSA.TopicWiseQuestions.Tree;

public class MorrisTraversal {
    public List<Integer> inorder(MyTreeNode root, List<Integer> list){
        // case 0: if root is null return the same list
        if(root == null) return list;

        // case 1: no left child
            // process the node and then move to the right child
        if(root.left == null){
            // System.out.println(root.data);
            list.add(root.data);
            return inorder(root.right, list);
        }

        // case 2: if left child 
            // move to the end of the right subtree of the left child and connect its right node with current element
            // and then try to process the left child
        
            // if on traversing for the right subtree you reach on to the same current node then 
            // disconnect the right node next with the currect node and process the node itself
        if(root.left != null){
            MyTreeNode children = root.left; // not null`
            while(children != null && (children.right != null && children.right != root)){
                children = children.right;
            }
            if (children.right == null) {
                children.right = root;
                return inorder(root.left, list);
            }
            if(children.right == root){
                children.right = null;
                // System.out.println(root.data);
                list.add(root.data);
                return inorder(root.right, list);
            }
        }
        return list;
    }
}
