# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = None
        if l1 is None and l2 is None:
            return head
        
        elif l1 is None:
            return l2
        
        elif l2 is None:
            return l1
        
        else:
            if l1.val <= l2.val:
                sorting = l1
                l1 = sorting.next
            else:
                sorting = l2
                l2 = sorting.next
            head = sorting
            
            while l1 and l2:
                if l1.val <= l2.val:
                    sorting.next = l1
                    sorting = l1
                    l1 = sorting.next
                else:
                    sorting.next = l2
                    sorting = l2
                    l2 = sorting.next
            if l1 is None:
                sorting.next = l2
            if l2 is None:
                sorting.next = l1
            return head
