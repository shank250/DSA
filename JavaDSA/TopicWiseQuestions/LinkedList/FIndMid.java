import java.util.Stack;

class Node{
    int data;
    Node next;
    Node(int data){
        this.data = data;
        this.next = null;
    }
    Node(){
        this.data = 0;
        this.next = null;
    }
    void add(int data){
        Node temp = this;
        while(temp.next != null){
            temp = temp.next;
        }
        temp.next = new Node(data);
    }
    
    Node findMid(Node head){
        if(head == null|| head.next == null){
            return head;
        }

        Node slow = head, fast = head;

        while(fast != null && fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }

        slow = slow.next;
        return slow;
    }


    public static void main(String[] args) {
        Node list = new Node(1);
        list.next = new Node(2);
        list.next.next = new Node(3);
        // list.next.next.next = new Node();

        System.out.println(list.findMid(list).data);
        // System.out.println();
        Stack<Integer> st = new Stack<>();
    }

}