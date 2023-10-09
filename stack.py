from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        if self.top:
            self.top = self.top.next
            self._size -= 1
        else: 
            raise IndexError('Erro')

    def peek(self):
        return self.top.data

    def __len__(self):
        if self.top:
            return self._size
        raise IndexError('Erro')

    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        r = ''
        pointer = self.top
        while pointer:
            r += str(pointer.data) + '\n'
            pointer = pointer.next
        return r[0:-3]