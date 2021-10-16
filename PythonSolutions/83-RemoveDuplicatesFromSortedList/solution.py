# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        current = head
        
        while current is not None and current.next is not None:
            # If current node value is same as next value:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head
            
        
