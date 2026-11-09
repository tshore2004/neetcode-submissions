# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        min_heap = []
        for i, linkedList in enumerate(lists):
            curr = linkedList
            if curr != None:
                heapq.heappush(min_heap, [curr.val, i, curr])
        while min_heap:
            small = heapq.heappop(min_heap)
            tail.next = small[2]
            tail = tail.next
            if small[2].next:
                heapq.heappush(min_heap, [small[2].next.val, small[1], small[2].next])

        return dummy.next