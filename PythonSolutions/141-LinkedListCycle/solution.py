# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        
        if head.next == head:
            return True
        
        fast = slow = head
        
        while slow and fast:
            fast = fast.next
            if fast == slow:
                return True
            if fast == None:
                return False
            fast = fast.next
            if fast == slow:
                return True
            slow = slow.next
        return False
            
        
