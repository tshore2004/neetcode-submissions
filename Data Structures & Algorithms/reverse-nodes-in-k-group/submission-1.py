# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
         


        # Reverse
        dummy = ListNode()
        tail = dummy
        curr = head
        
        # check groups
        while curr:
            i, t = 0, 0
            scout = curr
            while t < k:
                if scout == None:
                    break
                scout = scout.next
                t += 1
            if t < k:
                tail.next = curr
                break
            # reverse group
            old = curr
            prev = None
            while i < k and curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
                i+=1
            tail.next = prev
            tail = old

        return dummy.next
