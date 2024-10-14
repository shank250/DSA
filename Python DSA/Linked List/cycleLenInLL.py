#  Find length of Loop 
class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next

def lengthOfLoop(head: Node) -> int:
    def find_intersection(head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return slow 

        return None  

    def cycle_length(intersection):
        current = intersection.next
        length = 1

        while current != intersection:
            current = current.next
            length += 1

        return length

    intersection = find_intersection(head)

    if intersection:
        return cycle_length(intersection)
    else:
        return 0