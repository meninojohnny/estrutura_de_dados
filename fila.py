from node import Node

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elem):
        node = Node(elem)
        if self.last is None:
            self.last = node
        else: 
            self.last.next = node
            self.last = node
        
        if self.first is None:
            self.first = node
        self._size += 1

    def pop(self):
        if self.first:
            self.first = self.first.next
            self._size -= 1
        else:
            raise IndexError('Erro')
        
    def peek(self):
        return self.first.data
        
    def __len__(self):
        return self._size
    
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        r = ''
        pointer = self.first
        while pointer:
            r += str(pointer.data) + ' '
            pointer = pointer.next
        return r