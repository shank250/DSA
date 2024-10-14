# Find pairs with given sum in doubly linked list


class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


# def findPairs(head: Node, k: int) -> [[int]]:
#     ll, rtn = [], []
#     tmphead = head
#     while head:
#         ll.append(head.data)
#         head = head.next
#     if len(ll) % 2 == 0:
#         rgn = len(ll) // 2
#     else:
#         rgn = (len(ll) // 2)+ 1
#     for i in range(rgn):
#         ll.pop(i)
#         if (k - ll[i-1]) in ll:
#             rtn.append([ll[i-1], k - ll[i-1]])
#         ll.append(ll[i])
#     return rtn
# def findPairs(head: Node, k: int) -> [[int]]:
#     ll, rtn = [], []
    
#     # Convert linked list to list
#     while head:
#         ll.append(head.data)
#         head = head.next
    
#     # Iterate over the list to find pairs
#     for i in range(len(ll) - 1):
#         for j in range(i + 1, len(ll)):
#             if ll[i] + ll[j] == k:
#                 rtn.append([ll[i], ll[j]])
    
#     return rtn
def findPairs(head: Node, k: int) -> [[int]]:
    seen = set()
    rtn = []

    while head:
        complement = k - head.data

        if complement in seen:
            rtn.append([head.data, complement])

        seen.add(head.data)
        head = head.next

    return rtn