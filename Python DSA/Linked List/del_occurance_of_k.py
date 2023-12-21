#  Delete all occurrences of a given key in a doubly linked list 
class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def deleteAllOccurrences(head: Node, k: int) -> Node:
    rtnhead = None
    counter = 0
    while head:
        try:
            if head.data == k:
                if head.prev == None:
                    head.next.prev = None
                else:
                    head.prev.next = head.next
                if head.next == None:
                    head.prev.next = None
                else:
                    head.next.prev = head.prev
            else:
                if counter == 0:
                    rtnhead = head
                    counter += 1
            head = head.next
        except:
            return rtnhead
    return rtnhead
