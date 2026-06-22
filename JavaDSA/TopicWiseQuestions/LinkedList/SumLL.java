/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        /*
         * Here we have simply did what the question stated!
         */
        int carry = 0, num1, num2;
        ListNode tmpHead = new ListNode(-1), orgHead = tmpHead;
        
        while(!(l1 == null && l2 == null && carry == 0)){
            if(l1 != null){
                num1 = l1.val;
                l1 = l1.next;
            }else{
                num1 = 0;
            }
            if(l2 != null){
                num2 = l2.val;
                l2 = l2.next;
            }else{
                num2 = 0;
            }
            System.out.println("ok");
            ListNode head = new ListNode((carry + num1 + num2) % 10);
            tmpHead.next = head;
            tmpHead = head;
            carry = (carry + num1 + num2)/10;
        }

        return orgHead.next;
    }
}