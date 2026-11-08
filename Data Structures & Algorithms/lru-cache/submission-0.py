class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:
    def __init__(self, capacity: int):
        self.LRUCache = {}
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.LRUCache:
            Node = self.LRUCache[key]
            self.remove(Node)
            self.add(Node)
            return Node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.LRUCache:
            Node = self.LRUCache[key]
            Node.val = value
            self.remove(Node)
            self.add(Node)
        else:
            newNode = ListNode(key, value)
            self.LRUCache[key] = newNode
            self.add(newNode)
            if len(self.LRUCache) > self.capacity:
                lru = self.tail.prev
                self.remove(lru)
                del self.LRUCache[lru.key]

    def remove(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    def add(self, node: ListNode) -> None:
        nextNode = self.head.next
        node.prev = self.head
        node.next = nextNode
        self.head.next = node
        nextNode.prev = node

            