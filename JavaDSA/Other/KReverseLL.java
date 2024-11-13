package Other;

// public class Node{
//     int val;
//     Node next;
//     public Node(int val) {
//         this.val = val;
//     }
// }

public class KReverseLL {
    public static Node reverse(Node head, int k){
        if(head == null || head.next == null) return head;

        Node prev = head;
        Node cur = head.next;

        while(k > 0 && prev != null && cur != null){
            Node temp = cur.next;

            cur.next = prev;
            prev = cur;
            cur = temp;
        }

        // head.next = temp;

        return new Node(2);
    }
    

    public static Node reverseK(Node head, int k){
        return new Node(2);
    }
}
