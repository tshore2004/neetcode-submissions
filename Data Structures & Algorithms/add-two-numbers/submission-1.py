# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        dummy = ListNode(0)
        tail = dummy
        curr1 = l1
        curr2 = l2
        # add
        carry = 0
        while curr1 or curr2 or carry > 0:
            val1 = curr1.val if curr1 is not None else 0
            val2 = curr2.val if curr2 is not None else 0
            total = val1 + val2 + carry
            sums = total % 10
            carry = total // 10
            tail.next = ListNode(sums)
            tail = tail.next
            # print (curr1.val + curr2.val)
            print (tail.val)
            curr1 = curr1.next if curr1 is not None else None
            curr2 = curr2.next if curr2 is not None else None

        
        return dummy.next
        # reverse

