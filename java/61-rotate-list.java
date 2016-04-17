/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    // O(N) Solution
    // TODO: Merge connectEndToHead with getLength to increase run-time performance. 
    
    public ListNode rotateRight(ListNode head, int k) {
        // Steps:
        // 1. Get length of list to compute index of post-rotation list head
        // 3. Connect list `end` node with `head` to make circular list
        // 4. Disconnect link that connects to post-rotation list head
        // 5. Return post-rotation list head
        
        ListNode current = head;
        ListNode newHead;
        
        int length = this.getLength(head); 
        if(length < 2) return head; // Check if list is long enough to be rotated
        
        int newHeadIndex = length-(k%length); 
        if(newHeadIndex == 0) return head; // Check if list needs to be rotated
        
        int i = 0;
        while(i < newHeadIndex-1) {
            i++;
            current = current.next;
        }
        
        this.connectEndToHead(head);
        newHead = current.next;
        current.next = null;
        return newHead;
    }
    
    private void connectEndToHead(ListNode head) {
        ListNode current = head;
        if(head == null) return;
        
        while(current.next != null) {
            current = current.next;
        }
        current.next = head;
    }
    
    private int getLength(ListNode head) {
        ListNode current = head;
        int length = 0;
        
        while(current != null) {
            length++;
            current = current.next;
        }
        return length;
    }
}
