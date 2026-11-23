# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(q, (node.val, i, node))
        
        dummy = ListNode()
        cur = dummy

        while q:
            val, i, node = heapq.heappop(q)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(q, (node.next.val, i, node.next))
        
        return dummy.next