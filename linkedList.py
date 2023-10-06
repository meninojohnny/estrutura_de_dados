from linkedList import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            pointer = self.head
            while self.head:
                pointer = pointer.next
            pointer.next = Node(elem)
            self._size = self._size + 1
        else:
            self.head = Node(elem)
            self._size = self._size + 1