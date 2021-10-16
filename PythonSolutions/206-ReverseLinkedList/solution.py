# https://leetcode.com/problems/reverse-linked-list/ 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        
        current = head
        prev = next = None
        
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        head = prev
        return head
            
        
