class Solution:
    def isPalindrome(self, head):
        slow = fast = head

        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        fast = slow.next

        prev = head
        current = prev.next
        prev.next = None

        while current.next is not fast:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp

        while fast is not None:
            if head.val is not fast.val:
                return False
            head = head.next
            fast = fast.next
        
        return True