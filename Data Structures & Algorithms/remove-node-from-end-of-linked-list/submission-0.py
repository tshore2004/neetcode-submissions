# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current = head
        # find count
        while current:
            current = current.next
            count += 1
        # print (count)
        N = count - n
        curr2  = head
        new = None
        count = 0
        # remove
        while curr2:
            if N == 0:
                return head.next
            if count == N-1:
                # If I want to remove this skip
                curr2.next = curr2.next.next
            else:
                curr2 = curr2.next
            count += 1
        
        return head
