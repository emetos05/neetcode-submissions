class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.value
            i += 1
            curr = curr.next

        return -1
        

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode
        if not newNode.next:
            self.tail = newNode
        

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode
        

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True

        return False
        

    def getValues(self) -> List[int]:
        allNodes = []
        curr = self.head.next
        while curr:
            allNodes.append(curr.value)
            curr = curr.next

        return allNodes
        
