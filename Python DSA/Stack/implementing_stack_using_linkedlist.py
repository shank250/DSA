class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Stack:
    def __init__(self):
        self.size = 0
        self.top = None
        
    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def push(self, data):
        self.node = Node(data=data, next_node=self.top)
        self.top = self.node
        self.size += 1

    def pop(self):
        self.top = self.top.next
        self.size -= 1

    def getTop(self):
        return self.top