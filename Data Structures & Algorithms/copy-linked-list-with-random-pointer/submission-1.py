"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        retrieve = {}
        current = head

        while current:
            cloned = Node(current.val)
            retrieve[current] = cloned
            current = current.next
        
        current = head
        while current:
            cloned_current = retrieve[current]
            cloned_current.next = retrieve.get(current.next)
            cloned_current.random = retrieve.get(current.random)

            current = current.next
        if head == None:
            return head
        return retrieve[head]