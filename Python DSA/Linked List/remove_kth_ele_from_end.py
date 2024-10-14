'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

# def removeKthNode(head, k):    
#     thead = head
#     ele = []
#     while thead:
#         ele.append(thead.data)
#         thead = thead.next
#     remove = ele[-(k-1)]
#     thead = head
#     prev = head
#     while thead:
#         if thead.data == remove && counter == 0:
#             head = thead.next
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

def removeKthNode(head, k):
    slow_pointer = head
    fast_pointer = head
    prev = None

    for _ in range(k):
        fast_pointer = fast_pointer.next
    while fast_pointer:
        prev = slow_pointer
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next
    if not prev:
        return head.next
    prev.next = slow_pointer.next
    return head
