from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)
            self._size += 1
        else:
            self.head = Node(elem)
            self._size += 1

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if self.head:
            pointer = self._getnode(index)  
            return pointer.data
        
    def __setitem(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index - 1)
            node.next = pointer.next
            pointer.next = node

    def _getnode(self, index): 
        pointer = self.head
        for i in range(index):
            pointer = pointer.next
        if pointer:
            return pointer
        else:
            raise IndexError('Erro')  

    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index - 1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1

    def remove(self, elem):
        if self.head == None:
            raise ValueError('Erro')
        elif self.head.data == elem:
            self.head = self.head.next
        else:
            pointer = self.head.next
            ancestor = self.head
            for i in range(self.index(elem) - 1):
                if pointer:
                    pointer = pointer.next
                    ancestor = ancestor.next
            ancestor.next = pointer.next
            pointer.next = None
        self._size -+ 1
    
    def index(self, elem):
        i = 0
        pointer = self.head
        while pointer:
            if (pointer.data == elem):
                return i
            pointer = pointer.next
            i += 1
        raise IndexError('Erro')

    def __repr__(self):
        r = ''
        pointer = self.head
        while pointer:
            r += str(pointer.data) + ' -> '
            pointer = pointer.next
        return r
    
    def __str__(self):
        return self.__repr__()