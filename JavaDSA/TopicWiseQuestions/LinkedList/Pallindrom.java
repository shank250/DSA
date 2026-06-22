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
    public boolean isPalindrome(ListNode head) {
        /* 
         * find the mid of the linkedlist
         * disconnect the linked list in two halves
         * then reverse the linkedlist of the 2nd half after slow ptr
         * just traverse both the ll simultaneously.
         */
        ListNode slow = head, fast = head, prev;
        while(fast != null && fast.next != null){
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        
    }
}