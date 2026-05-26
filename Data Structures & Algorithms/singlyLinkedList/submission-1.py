class ListNode:
    def __init__(self, val, next_node = None):
        self.value = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        cur =  self.head.next
        i = 0
        while cur:
            if i == index:
                return cur.value
            cur = cur.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        if not self.head.next:
            self.tail = new_node
        self.head.next = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0
        while i < index and cur:
            cur = cur.next
            i += 1
        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        res = []
        cur = self.head.next
        while cur:
            res.append(cur.value)
            cur = cur.next
        return res
