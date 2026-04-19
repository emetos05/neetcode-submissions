class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:    
    def __init__(self):
        # Dummy nodes
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        newNode = ListNode(value)
        lastNode = self.tail.prev
        lastNode.next = newNode
        newNode.prev = lastNode
        newNode.next = self.tail
        self.tail.prev = newNode

    def appendleft(self, value: int) -> None:
        newNode = ListNode(value)
        firstNode = self.head.next
        self.head.next = newNode
        newNode.next = firstNode
        newNode.prev = self.head
        firstNode.prev = newNode        

    def pop(self) -> int:        
        if self.isEmpty():
            return -1
        lastNode = self.tail.prev
        val = lastNode.val

        prevNode = lastNode.prev
        prevNode.next = self.tail
        self.tail.prev = prevNode

        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        firstNode = self.head.next
        val = firstNode.val

        nextNode = firstNode.next
        nextNode.prev = self.head
        self.head.next = nextNode
        
        return val

        
        