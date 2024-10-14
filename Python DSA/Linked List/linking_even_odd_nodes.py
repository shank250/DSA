'''
Following is the structure of the Node class already defined:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

# def segregateEvenOdd(head):
#     thead = head
#     even, odd = [], []
#     while thead:
#         if (thead.data)%2 == 0:
#             even.append(thead)
#         else:
#             odd.append(thead)
#     thead = thead.next
#     tempehead, tempohead = None, None
#     for ehead in even:
#         if tempehead == None:
#             tempehead = ehead
#         else:
#             tempehead.next = ehead
#             tempehead = ehead
#     ehead.next = odd[0]
#     for ohead in odd:
#         if tempohead == None:
#             tempohead = ohead
#         else:
#             tempohead.next = ohead
#             tempohead = ohead
#     return even[0]
def segregateEvenOdd(head):
    if not head or not head.next:
        return head

    even_head, odd_head = None, None
    even_tail, odd_tail = None, None

    current = head

    while current:
        if current.data % 2 == 0:
            if not even_head:
                even_head = current
                even_tail = current
            else:
                even_tail.next = current
                even_tail = current
        else:
            if not odd_head:
                odd_head = current
                odd_tail = current
            else:
                odd_tail.next = current
                odd_tail = current

        current = current.next

    if even_tail:
        even_tail.next = odd_head
        odd_tail.next = None  # Ensure the last node of the odd list points to None
        return even_head
    else:
        return odd_head