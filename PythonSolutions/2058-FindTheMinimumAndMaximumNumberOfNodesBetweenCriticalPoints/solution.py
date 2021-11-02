# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head is None:
            return
        
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        if length <= 2:
            return [-1, -1]
            
        
        critical_points = []
        minima = []
        maxima = []
        
        current1 = current2 = head
        dummy = ListNode(math.inf)
        
        dummy.next = head
        prev1 = prev2 = dummy
        index1 = index2 = 0
        
        while current1:
            index1 += 1
            if current1.next:
                if current1.val > current1.next.val and current1.val > prev1.val:
                    maxima.append(index1)
            prev1 = current1
            current1 = current1.next
        print(maxima)
        
        while current2:
            index2 += 1
            if current2.next:
                if current2.val < current2.next.val and current2.val < prev2.val:
                    minima.append(index2)
            prev2 = current2
            current2 = current2.next
        print(minima)
        if 1 in minima:
            minima.remove(1)
        
        criticals = minima + maxima
        criticals.sort()
        print(criticals)
        n = len(criticals)
        if len(criticals) < 2:
            return [-1, -1]
        max_distance = max(criticals) - min(criticals)
        # min_distance = criticals[-1] - criticals[-2]
        
        min_distance = math.inf
        
        for i in range(n-1):
            if criticals[i+1] - criticals[i] < min_distance:
                min_distance = criticals[i+1] - criticals[i]
        return[min_distance, max_distance]
        
        
                    
            
            
            
        
