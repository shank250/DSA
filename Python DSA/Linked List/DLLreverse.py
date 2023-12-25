'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
'''

def reverseDLL(head):
    headt = head
    data = []
    while headt:
        data.append(headt.data)
        headp = headt
        headt = headt.next
    headp = head
    while headp:
        headp.data = data.pop(-1)
        headp = headp.next
    return head