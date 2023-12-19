'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def firstNode(head):
    visited = []
    while head:
        if head in visited:
            return head
        visited.append(head)
        
        head = head.next
    return None