import java.util.*;

// Definition for singly-linked list.

public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}


class SwapNodesInPairs {
    public ListNode swapPairs(ListNode head) {
        ListNode prev = new ListNode(0);
        ListNode newHead = prev;
        Stack<ListNode> stack = new Stack<>();

        int noOfNodesProc = 0;
        while(head != null){
            while(head != null){
                if(noOfNodesProc == 2){
                    noOfNodesProc = 0;
                    break;
                }
                
                stack.add(head);
                head = head.next;
                noOfNodesProc++;
            }
            while(stack.size() != 0){
                prev.next = stack.pop();
                prev = prev.next;
            }
        }

        return newHead.next;
    }
}


// create one dummy node name it previous 
    // add two nodes into the stack if two are present else add only one node
    // now pop two elemwnts form the stack if present and add then to the older prevNode
//  repeat the same until the ll is processed